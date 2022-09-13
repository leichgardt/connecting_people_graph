from pydantic import BaseModel

from src.models.communication import PeopleCommunication


class Journal(BaseModel):
    communications: list[PeopleCommunication]
