import pandas as pd


def driver_champions_per_year():
    races = pd.read_csv('Data/races.csv')
    drivers = pd.read_csv('Data/drivers.csv')
    driver_standings = pd.read_csv('Data/driver_standings.csv')
    driver_position = drivers.merge(driver_standings,left_on='driverId',right_on='driverId',how = 'left')
    driver_position = driver_position.merge(races,on = 'raceId',how = 'left')
    champions_df = driver_position.groupby(['nationality','year','surname'])[['points','wins']].max().sort_values('points',ascending = False).reset_index()
    champions_df.drop_duplicates(subset=['year'], inplace=True)
    champions_df = champions_df.sort_values(by="year")
    return champions_df[:-1]


def driver_champions_per_nation():
    champions = driver_champions_per_year()
    champions = champions.groupby(['nationality'], as_index=False)[['year']].count()
    champions.rename(columns={'year': 'titles'}, inplace=True)
    return champions


def constructor_champions_per_year():
    races = pd.read_csv('Data/races.csv')
    constructors = pd.read_csv('Data/constructors.csv')
    constructor_standings = pd.read_csv('Data/constructor_standings.csv')
    constuctor_position = constructors.merge(constructor_standings,left_on='constructorId',right_on='constructorId',how = 'left')
    constuctor_position = constuctor_position.merge(races,on = 'raceId',how = 'left')
    # st.table(constuctor_position)
    champions_df = constuctor_position.groupby(['nationality','year', 'RealName'])[['points','wins']].max().sort_values('points',ascending = False).reset_index()
    # st.table(champions_df)
    champions_df.drop_duplicates(subset=['year'], inplace=True)
    champions_df = champions_df.sort_values(by="year")
    champions_df.rename(columns={'name_x': 'constructor'}, inplace=True)
    champions_df['year'] = champions_df['year'].apply(lambda x: round(x))
    return champions_df[:-1]



def constructor_champions_per_nation():
    champions = constructor_champions_per_year()
    champions = champions.groupby(['nationality'], as_index=False)[['year']].count()
    champions.rename(columns={'year': 'titles'}, inplace=True)
    return champions
