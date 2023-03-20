import pandas as pd

def driver_standings_per_season(season):
    driver_standings = pd.read_csv('Data/driver_standings.csv')
    drivers = pd.read_csv('Data/drivers.csv')
    race = pd.read_csv('Data/races.csv')
    grand_prixes = race[race['year'] == season]
    raceIds = grand_prixes['raceId']
    mask = driver_standings.raceId.isin(raceIds)
    driver_standings = driver_standings.loc[mask, : ]
    driver_standings = pd.merge(driver_standings, race[['raceId', 'round']], on="raceId", how="left")
    driver_standings.sort_values(by=['round'], inplace=True)
    driver_standings['driver_name'] = driver_standings['driverId'].apply(lambda x: drivers[drivers['driverId'] == x].iloc[0].surname)

    return driver_standings

