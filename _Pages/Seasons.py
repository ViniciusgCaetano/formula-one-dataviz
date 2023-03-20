import streamlit as st
from DataProcessing import seasons, standings_per_season
from Plots.standing_graphs import standing_graph

def render_page():
    st.title('Seasons')
    season_year = st.selectbox('Select a Season', seasons.seasons())
    #st.table(standings_per_season.driver_standings_per_season(season_year))
    st.plotly_chart(standing_graph(season_year), use_container_width=True)