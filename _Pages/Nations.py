import streamlit as st
from DataProcessing.Nation_graphs import constructors_per_nation, drivers_per_nation

def render_page():
    st.title("Nations")
    
    col1, col2 = st.columns(2)

    col1.header('Teams By Nation')
    col1.table(constructors_per_nation()[:10])

    col2.header('Drivers By Nation')
    col2.table(drivers_per_nation()[:10])

    