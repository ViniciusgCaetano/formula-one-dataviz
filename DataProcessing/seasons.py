import pandas as pd

def seasons():
    df = pd.read_csv('Data/seasons.csv')
    df.sort_values(by='year', inplace=True, ascending=False)
    return df[1:]