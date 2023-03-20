import pandas as pd

def constructors_per_nation():
    df = pd.read_csv('Data/constructors.csv')
    df = df.groupby(['nationality'], as_index=False).count()
    df = df.sort_values(by=['RealName'], ascending=False)
    df = df.reset_index(drop=True)
    df = df[['nationality', 'RealName']]
    df.rename(columns={'RealName': 'Constructors'}, inplace=True)


    return df

def drivers_per_nation():
    df = pd.read_csv('Data/drivers.csv')
    df = df.groupby(['nationality'], as_index=False).count()
    df = df.sort_values(by=['surname'], ascending=False)
    df = df[['nationality', 'code']]
    df.rename(columns={'code': 'Drivers'}, inplace=True)
    df = df.reset_index(drop=True)

    return df