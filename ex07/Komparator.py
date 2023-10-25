from ex06.MyPlotLib import MyPlotLib
import matplotlib.pyplot as plt
import pandas as pd

class Komparator(MyPlotLib):
    def __init__(self, df: pd.DataFrame):
        self.data = df
        super().__init__()
        return

    def compare_box_plots(self, categorical_var, numerical_var):
        self.data.boxplot(numerical_var, by=categorical_var)

    def density(self, categorical_var, numerical_var):
        self.data.groupby(categorical_var)[numerical_var].plot.density()
        plt.legend()

    def compare_histograms(self, categorical_var, numerical_var):
        for grp, frame in self.data.groupby(categorical_var)[numerical_var]:
            plt.hist(frame, label=grp, alpha=.5, color='steelblue')
        plt.legend()


kp = Komparator(pd.read_csv('athlete_events.csv'))
kp.compare_histograms('Sex', 'Year')