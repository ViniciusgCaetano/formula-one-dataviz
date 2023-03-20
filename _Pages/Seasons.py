import streamlit as st
from DataProcessing import seasons
from Plots.standing_graphs import driver_standing_graph, constructor_standing_graph

def render_page():
    st.title('Seasons')
    season_year = st.selectbox('Select a Season', seasons.seasons())
    #st.table(standings_per_season.driver_standings_per_season(season_year))
    exp = st.expander('Accumulated Points by Race (Drivers)')
    exp.plotly_chart(driver_standing_graph(season_year), use_container_width=True)

    exp = st.expander('Accumulated Points by Race (Constructors)')
    exp.plotly_chart(constructor_standing_graph(season_year), use_container_width=True)