import pandas as pd

def proportion_by_sport(df: pd.DataFrame, year: int, sport: str, gender: str):
    subset = df[(df['Year'] == year) & (df['Sex'] == gender)]
    return len(subset[df['Sport'] == sport]) * 100 / len(subset)