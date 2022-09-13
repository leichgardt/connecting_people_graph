from pathlib import Path

from src.database import BaseStorage
from src.schemas.graph import SocialGraph
from src.models.communication import PeopleCommunication


class SocialCommunicator:
    """
    Класс социальных связей. Предоставляет доступ к графу социальных коммуникаций, в котором вершины являются
    пользователями, а ребра - связью между ними. Вес ребра описывает количество коммуникаций между людьми.

    Класс способен работать с различными представлениями хранилища графа (в данный момент реализован
    только MemoryStorage).
    """

    def __init__(self, storage: BaseStorage):
        self.storage = storage

    def get_relationship_communications(self, communication: PeopleCommunication):
        """Получить количество коммуникаций между парой человек."""
        return self.storage.get_edge_weight(communication.person_1_id, communication.person_2_id)

    def get_person_relationships(self, person_id: int):
        """Получить все отношения человека с их количеством коммуникаций."""
        return self.storage.get_neighbor_nodes(person_id)

    def add_new_communication(self, communication: PeopleCommunication):
        """Добавить новую коммуникацию между парой человек."""
        self.storage.save_edge(communication.person_1_id, communication.person_2_id)

    def get_social_communication_graph(self, filename: str = None) -> tuple[list, dict, Path]:
        """Получить граф в виде матрицы смежности, его метаданные, путь к файлу с изображением."""
        matrix, stat = self.storage.get_all_data()
        graph = SocialGraph(matrix, stat)
        filepath = graph.draw_graph(filename)
        return matrix, stat, filepath
