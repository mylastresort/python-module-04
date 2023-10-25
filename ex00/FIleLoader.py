import pandas as pd

class FileLoader:
    def load(self, path):
        df = pd.read_csv(path)
        print('Loading dataset of dimensions {} x {}'.format(
            df.shape[0], df.shape[1]))
        return df

    def display(self, df: pd.DataFrame, n: int):
        print(df.iloc[:n])