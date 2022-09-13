"""
Модуль класса MemoryStorage для хранения графа в оперативной памяти.
"""

from src.database.base import BaseStorage
from src.schemas.matrix import AdjacencyMatrix


class MemoryStorage(BaseStorage):
    """
    Класс работы с графом и хранением его в памяти. Граф хранится в виде матрицы смежности.
    """

    def __init__(self):
        self._relationship_matrix = AdjacencyMatrix()

    def get_edge_weight(self, node1, node2):
        return self._relationship_matrix[node1, node2]

    def save_edge(self, node1, node2):
        if (node1, node2) not in self._relationship_matrix:
            self._relationship_matrix[node1, node2] = 0
        self._relationship_matrix[node1, node2] += 1

    def get_neighbor_nodes(self, node):
        return self._relationship_matrix[node]

    def get_all_data(self) -> tuple[list, dict]:
        return self._relationship_matrix.get_matrix(), self._relationship_matrix.get_stat()


if __name__ == '__main__':
    m = AdjacencyMatrix()
    m[0, 1] = 1
    print(m[0] == {1: 1})
    print(m[0, 1] == 1)
    print(0 in m)
    print(1 in m)
    print((0, 1) in m)
    print((1, 0) in m)
