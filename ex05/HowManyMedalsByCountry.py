# fl = FileLoader()
# df = fl.load('athlete_events.csv')
# country = 'CHN'
# medals = ['Gold', 'Silver', 'Bronze']
# query = df[(df['NOC'] == country) & df['Medal'].isin(medals)]
# by_years = query.groupby('Year')
# by_years.apply(lambda yr: yr.groupby('Medal')['Medal'].count().to_dict()).to_dict()