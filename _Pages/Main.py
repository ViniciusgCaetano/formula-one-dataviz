import streamlit as st

def render_page():     
    st.title('Formula One DataViz')
    st.markdown("""<div style="text-align: justify">Check out my Streamlit App-a-Thon project, which provides fascinating insights into the F1 World Championship. 
    The project offers a range of visualizations that display interesting information about the championship, such as the number of wins by each team, the position of drivers over time, and the 
    distribution of lap times. You can explore the data using various types of charts, including bar charts, line charts, scatter plots, and radar charts. With this project, you'll gain a deeper 
    understanding of the F1 World Championship and its history.</div>""", unsafe_allow_html=True)
