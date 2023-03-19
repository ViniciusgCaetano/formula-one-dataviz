from DataProcessing.nation_datasets import constructors_per_nation, drivers_per_nation
import plotly.graph_objects as go
import plotly.express as px

def constructors_per_nation_graph():
    df = constructors_per_nation()[:10]

    constructor_figure = go.Figure(go.Bar(x=df['nationality'], y=df['Constructors'], showlegend=False))
    constructor_figure.update_layout({"margin":{"t": 0}})
    constructor_figure.update_traces(marker_color='rgb(179,0,0)')

    return constructor_figure

def drivers_per_nation_graph():
    df = drivers_per_nation()[:10]

    driver_figure = go.Figure(go.Bar(x=df['nationality'], y=df['Drivers'], showlegend=False))
    driver_figure.update_layout({"margin":{"t": 0}})
    driver_figure.update_traces(marker_color='rgb(179,0,0)')
    
    return driver_figure