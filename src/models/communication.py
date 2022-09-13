"""
Модель коммуникации пары людей.
"""

from pydantic import BaseModel


class PeopleCommunication(BaseModel):
    """
    Модель отношений между парой человек.
    """
    person_1_id: int
    person_2_id: int

    def __init__(self, **kwargs):
        """
        Отношения строятся всегда в порядке person1.id < person2.id (это связано с логикой взаимодействия
        с матрицей смежности).
        """
        super().__init__(**kwargs)
        if self.person_1_id == self.person_2_id:
            raise ValueError('Identical person ID. It seems same person has been passed twice.')
        elif self.person_1_id > self.person_2_id:
            self.person_1_id, self.person_2_id = self.person_2_id, self.person_1_id


if __name__ == '__main__':
    rel = PeopleCommunication(person_1_id=1, person_2_id=2)
    print(rel)
