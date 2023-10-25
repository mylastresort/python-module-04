import pandas as pd

def youngest_fellah(df: pd.DataFrame, year: int):
    return dict((df[df['Year'] == year].groupby('Sex').min('Age'))['Age'])