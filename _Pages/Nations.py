import streamlit as st
from DataProcessing.nation_datasets import constructors_per_nation, drivers_per_nation
from DataProcessing.champions import driver_champions_per_nation, constructor_champions_per_year, constructor_champions_per_nation
from Plots.nation_graphs import constructors_per_nation_graph, drivers_per_nation_graph




def render_page():
    st.title("Nations")
    exp = st.expander(label="Analyse a country", expanded=True)

    constructors_df = constructors_per_nation()
    drivers_df = drivers_per_nation()
    champions_per_nation_df = driver_champions_per_nation()
    constructor_champions_per_nation_df = constructor_champions_per_nation()

    nationality = exp.selectbox('Choose a nationality', constructors_df['nationality'])
    col1, col2, col3, col4 = exp.columns(4)

    try:
        driver_count = drivers_df[drivers_df['nationality'] == nationality].Drivers
    except TypeError:
        driver_count = 0

    try:
        constructor_count = constructors_df[constructors_df['nationality'] == nationality].Constructors
        int(constructor_count)
    except TypeError:
        constructor_count = 0

    try:
        champions_count = champions_per_nation_df[champions_per_nation_df['nationality'] == nationality].titles
        int(champions_count)
    except TypeError:
        champions_count = 0
    
    try:
        constructor_titles_count = constructor_champions_per_nation_df[constructor_champions_per_nation_df['nationality'] == nationality].titles
        int(constructor_titles_count)
    except TypeError:
        constructor_titles_count = 0

    col1.metric('Drivers', driver_count)

    col2.metric('Constructors', constructor_count)

    col3.metric('Driver Titles', champions_count)

    col4.metric('Constructor Titles', constructor_titles_count)

    col1, col2 = st.columns(2)

    col1.header('Teams By Nation')
    col1.plotly_chart(constructors_per_nation_graph(), use_container_width=True)

    col2.header('Drivers By Nation')
    col2.plotly_chart(drivers_per_nation_graph(), use_container_width=True)

 

   

  




    