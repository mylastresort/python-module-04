import pandas as pd

def how_many_medals(df: pd.DataFrame, name: str):
    # duplicate row may have to be deleted in future
    medals = ['Gold', 'Silver', 'Bronze']
    query = df[(df['Name'] == name) & df['Medal'].isin(medals)]
    by_years = query.groupby('Year')
    return by_years.apply(lambda yr: yr.groupby('Medal')['Medal'].count().to_dict()).to_dict()