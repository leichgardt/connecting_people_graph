"""
Модуль базового класса для работы с графом.
"""

from abc import abstractmethod, ABC


class BaseStorage(ABC):
    """
    Базовый класс взаимодействия с графом. Используйте для создания интерфейса.
    """

    @abstractmethod
    def get_edge_weight(self, node1: int, node2: int) -> int:
        """Получить вес ребра между узлами."""
        pass

    @abstractmethod
    def save_edge(self, node1: int, node2: int):
        """Создать ребро или увеличить вес ребра между узлами."""
        pass

    @abstractmethod
    def get_neighbor_nodes(self, node: int) -> dict[int, int]:
        """Получить все связанные узлы."""
        pass

    @abstractmethod
    def get_all_data(self) -> tuple[list, dict]:
        """
        Получить все данные графа. Первым элементом будет матрица смежности графа в виде списка списков, а вторым
        словарь со статистикой.
        """
        pass
