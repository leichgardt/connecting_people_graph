import os
from pathlib import Path
from urllib.parse import urlparse, urlsplit

from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.staticfiles import StaticFiles

from src.database import MemoryStorage
from src.network import SocialCommunicator
from src.models.journal import Journal
from src.models.communication import PeopleCommunication


root_path = Path(os.path.realpath(__file__)).parent
if not (path := (root_path / 'static')).exists():
    path.mkdir()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
storage = MemoryStorage()
communicator = SocialCommunicator(storage)


@app.on_event("startup")
def startup():
    """Создать стартовый граф коммуникаций при запуске приложения"""
    pairs = ((1, 2), (2, 3), (2, 4), (2, 3), (3, 4), (4, 5), (4, 1), (1, 3))
    journal = Journal(communications=[PeopleCommunication(person_1_id=i, person_2_id=j) for i, j in pairs])
    add_journal_communications(journal)


def add_journal_communications(journal: Journal):
    """Добавить коммуникации с журнала"""
    for comm in journal.communications:
        communicator.add_new_communication(comm)


@app.post("/new_communication_journal")
def add_new_communication(journal: Journal, background_task: BackgroundTasks):
    """Добавить новые коммуникации из json-журнала в коммуникатор, который сохранить их в хранилище."""
    background_task.add_task(add_journal_communications, journal)
    return {"message": "Journal accepted"}


@app.get("/graph")
def get_graph_data(request: Request):
    """Получить граф в виде матрицы смежности, его метаданные и ссылку на изображение графа"""
    matrix, meta, filepath = communicator.get_social_communication_graph()
    file_url = urlparse(os.path.relpath(filepath, root_path).replace("\\", "/")).path
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(str(request.url)))
    return {"data": {"matrix": matrix, "meta": meta, "url": base_url + file_url}}
