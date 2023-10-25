import pandas as pd

class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        self.data = df
        return

    def when(self, location: str):
        return self.data[self.data['City'] == location]['Year']

    def where(self, date):
        return self.data[self.data['Year'] == date]['Location']