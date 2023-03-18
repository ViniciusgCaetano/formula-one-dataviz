import streamlit as st
from DataProcessing.nation_datasets import constructors_per_nation, drivers_per_nation
import plotly.graph_objects as go




def render_page():
    st.title("Nations")
    st.markdown("Countries are a important factor in Formula One. ")
    
    col1, col2 = st.columns(2)

    col1.header('Teams By Nation')
    df = constructors_per_nation()[:10]

    constructor_figure = go.Figure(go.Bar(x=df['nationality'], y=df['Constructors'], showlegend=False))
    constructor_figure.update_layout({"margin":{"t": 0}})

    col1.plotly_chart(constructor_figure, use_container_width=True)

    col1.table(constructors_per_nation()[:10])

    col2.header('Drivers By Nation')
    df = drivers_per_nation()[:10]
    drivers_figure = go.Figure(go.Bar(x=df['nationality'], y=df['Drivers'], showlegend=False))
    drivers_figure.update_layout({"margin":{"t": 0}})


    col2.plotly_chart(drivers_figure, use_container_width=True)



    