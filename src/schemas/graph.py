import os
from io import StringIO
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx


class SocialGraph:
    """Класс для создания графа из матрицы смежности."""

    def __init__(self, matrix: list[list[int]], stat: dict):
        self.matrix = matrix
        self.keys = sorted(stat.keys())

    @property
    def data_frame(self) -> pd.DataFrame:
        """DataFrame из данных матрицы и ее мета данных."""
        csv_data = ','.join(str(k) for k in self.keys)
        for i in range(len(self.keys)):
            csv_data += f'\n{self.keys[i]},' + ','.join(str(line) for line in self.matrix[i])
        return pd.read_csv(StringIO(csv_data), index_col=0)

    def draw_graph(self, filename=None) -> Path:
        """Нарисовать граф и сохранить его в файл."""
        G = nx.Graph(self.data_frame.values)
        pos = nx.spring_layout(G)
        nx.draw(G, pos,
                node_size=500,
                labels={i: k for i, k in enumerate(self.keys)},
                with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
        filepath = Path(os.path.realpath(__file__)).parent.parent.parent / 'static' / 'images' / 'png'
        if not filepath.exists():
            filepath.mkdir(parents=True, exist_ok=True)
        fullpath = filepath / (filename or 'graph.png')
        if fullpath.exists():
            fullpath.unlink()
        plt.savefig(fullpath, format='png')
        return fullpath
