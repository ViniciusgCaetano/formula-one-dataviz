from DataProcessing.standings_per_season import driver_standings_per_season, constructor_standings_per_season
import plotly.graph_objects as go
import plotly.express as px

def driver_order(standings_per_season): 
    driver_order = standings_per_season.groupby('driver_name', as_index=False).max()
    driver_order.sort_values(by=['points'], inplace=True, ascending=False)
    return {k:v for (k,v) in zip(driver_order['driver_name'], range(1, len(driver_order['driver_name']) + 1))}


def constructor_order(standings_per_season): 
    constructor_order = standings_per_season.groupby('constructor_name', as_index=False).max()
    constructor_order.sort_values(by=['points'], inplace=True, ascending=False)
    return {k:v for (k,v) in zip(constructor_order['constructor_name'], range(1, len(constructor_order['constructor_name']) + 1))}



def driver_standing_graph(season):
    standings_per_season = driver_standings_per_season(season)
    d_order = driver_order(standings_per_season)
    standings_per_season['final_pos'] = standings_per_season['driver_name'].apply(lambda x: d_order[x])
    standings_per_season = standings_per_season.sort_values(['round', 'final_pos'])


    fig = px.line(standings_per_season, x="round", y="points", color="driver_name")

    fig.update_layout(title='Acumulated Points By Race (Driver)',
                    xaxis_title='Race',
                    yaxis_title='Points',
                    legend_title_text='Driver'
                   )

    
    return fig

def constructor_standing_graph(season):
    standings_per_season = constructor_standings_per_season(season)
    d_order = constructor_order(standings_per_season)
    standings_per_season['final_pos'] = standings_per_season['constructor_name'].apply(lambda x: d_order[x])
    standings_per_season = standings_per_season.sort_values(['round', 'final_pos'])


    fig = px.line(standings_per_season, x="round", y="points", color="constructor_name")

    fig.update_layout(title='Acumulated Points By Race (Constructor)',
                    xaxis_title='Race',
                    yaxis_title='Points',
                    legend_title_text='Constructor'
                   )
    return fig