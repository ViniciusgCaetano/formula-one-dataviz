import pandas as pd
from DataProcessing.champions import driver_champions_per_year, constructor_champions_per_year

def seasons():
    df = pd.read_csv('Data/seasons.csv')
    df.sort_values(by='year', inplace=True, ascending=False)
    return df[1:]

def _total_races(season_year):
    races = pd.read_csv('Data/races.csv')
    mask = races['year'] == season_year
    races = races[mask]
    total_races = races['round'].max()
    return total_races 

def _season_driver_winner(season_year):
    driver_champions =  driver_champions_per_year()
    mask = driver_champions['year'] == season_year
    season_champion = driver_champions[mask].iloc[0].surname
    return season_champion 

def _season_constructor_winner(season_year):
    constructor_champions =  constructor_champions_per_year()
    mask = constructor_champions['year'] == season_year
    season_champion = constructor_champions[mask].iloc[0].RealName
    return season_champion 


def metrics(season_year):
    season_dict = {}
    season_dict['Total Races'] = _total_races(season_year)
    season_dict['Champion Driver'] = _season_driver_winner(season_year)
    season_dict['Champion Constructor'] = _season_constructor_winner(season_year)
    return season_dict 

    

