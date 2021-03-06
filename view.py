
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        sns.set()

    def vis(self, df, x, y, type="line"):
        if type == "reg":
            sns.regplot(x=x, y=y, data=df)
        elif type == "scatter":
            sns.scatterplot(x=x, y=y, data=df)
        else:
            sns.lineplot(x=x, y=y, data=df)
        plt.show()

    def heatmap(self, df):
        # https://seaborn.pydata.org/generated/seaborn.heatmap.html
        heatmapData = pd.pivot_table(df, values='visitors',
                     index=['hour'],
                     columns='weekday')
        sns.heatmap(heatmapData, cmap="YlGnBu")
        plt.show()
