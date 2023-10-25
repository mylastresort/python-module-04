import matplotlib.pyplot as plt
import pandas as pd

class MyPlotLib:
    def histogram(self, data: pd.DataFrame, features: list[str]):
        for i, ft in enumerate(features, 1):
            plt.subplot(2, 2, i).hist(data[ft])
            plt.title(ft)
            plt.tight_layout()

    def density(self, data: pd.DataFrame, features: list[str]):
        data[features].plot.density()

    def pair_plot(self, data: pd.DataFrame, features: list[str]):
        pd.plotting.scatter_matrix(data[features])

    def box_plot(self, data: pd.DataFrame, features: list[str]):
        data[features].boxplot()