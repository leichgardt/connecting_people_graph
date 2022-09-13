"""
Модель представления матрицы смежности для хранения графа.
"""


class NodeConnections:
    """
    Класс связи вершины графа с другими вершинами и вес их ребра. Представляет только другие вершины, без основной,
    а также статистику связей (min, max, avg). Статистика обновляется при добавлении новых связей.
    """

    connections: dict[int, int]

    def __init__(self, relationships: dict[int, int] = None):
        self.connections = relationships or {}
        self._min = 1
        self._max = 0
        self._avg = .0

    def __setitem__(self, key, value):
        self.connections[key] = value
        self._min = min(self._min, value) if value > 0 else self._min
        self._max = max(self._max, value)
        self._avg = sum(con for con in self.connections.values() if con > 0) / len(self.connections)

    def __getitem__(self, item):
        return self.connections.get(item)

    def __contains__(self, item):
        return item in self.connections

    def __repr__(self):
        return f'NodeConnections({self.connections})'

    @property
    def min(self) -> int:
        """Минимальный вес ребер."""
        return self._min

    @property
    def max(self) -> int:
        """Максимальный вес ребер."""
        return self._max

    @property
    def avg(self) -> float:
        """Среднее значение веса ребер."""
        return self._avg


class AdjacencyMatrix:
    """
    Класс матрицы смежности графа, реализованный на словарях. Ключом может быть как узел, так и пара узлов в кортеже.
    >>> mtx = AdjacencyMatrix()
    >>> mtx[1, 3] = 1

    При запросе через один узел будет выдан словарь смежных узлов - ребер - с их весом.
    >>> mtx[1] == {3: 1}
    При запросе через два узла будет выдан вес ребра, соединяющего их.
    >>> mtx[1, 3] == 1
    Доступна проверка содержания.
    >>> (1, 3) in mtx
    >>> (3, 1) in mtx
    >>> 1 in mtx
    >>> 3 in mtx
    ...

    Атрибуты
    --------
    matrix : DictionaryAdjacencyMatrix_
        словарь отношений людей, содержащией словари связанных с ними отношениями людей и их силу (связи)
    """

    matrix: dict[int, NodeConnections]

    def __init__(self):
        self.matrix = {}

    def __setitem__(self, key: tuple[int, int], value: int):
        for node in key:
            if node not in self.matrix:
                self.matrix[node] = NodeConnections()
        self.matrix[key[0]][key[1]] = value
        self.matrix[key[1]][key[0]] = value

    def __getitem__(self, item: int | tuple[int, int]):
        if isinstance(item, int):
            return self.matrix.get(item).connections
        else:
            return self.matrix.get(item[0], NodeConnections())[item[1]]

    def __contains__(self, item: int | tuple[int, int]):
        if isinstance(item, int):
            return item in self.matrix
        else:
            return item[0] in self.matrix and item[1] in self.matrix[item[0]]

    def get_matrix(self) -> list:
        """Представить данные в виде матрицы смежности. Также возвращает статистику по связям."""
        matrix = [[0] * len(self.matrix) for _ in range(len(self.matrix))]
        keys = sorted(self.matrix.keys())
        for i, node1 in enumerate(keys):
            for node2, rel in self.matrix[node1].connections.items():
                j = keys.index(node2)
                matrix[i][j] = rel
        return matrix

    def get_stat(self) -> dict:
        """Получить статистику каждого узла по его связям."""
        stat = {}
        for node1 in sorted(self.matrix.keys()):
            stat[node1] = {'min': self.matrix[node1].min, 'max': self.matrix[node1].max, 'avg': self.matrix[node1].avg}
        return stat


if __name__ == '__main__':
    m = AdjacencyMatrix()
    m[1, 2] = 1
    m[1, 5] = 1
    m[2, 3] = 1
    m[2, 5] = 2
    m[4, 5] = 3
    m[4, 5] += 3

    print(len(m.matrix))
    print(m.matrix)
    list_matrix = m.get_matrix()
    matrix_stat = m.get_stat()
    print(matrix_stat.keys())
    for line in list_matrix:
        print(line)
