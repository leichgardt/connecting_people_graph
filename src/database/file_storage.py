"""
Модуль класса MemoryStorage для хранения графа в оперативной памяти.
"""

from src.database.base import BaseStorage


class FileStorage(BaseStorage):
    """
    Класс работы с графом и хранением его в памяти. Граф хранится в виде матрицы смежности.
    """

    def __init__(self, filename: str = None):
        self._filename = filename

    # def get_edge_weight(self, node1, node2):
    #     return self.relationships[node1, node2]
    #
    # def save_edge(self, node1, node2):
    #     if (node1, node2) not in self.relationships:
    #         self.relationships[node1, node2] = 0
    #     self.relationships[node1, node2] += 1
    #
    # def get_neighbor_nodes(self, node):
    #     return self.relationships[node]
    #
    # def get_all_data(self):
    #     return self.relationships.matrix
