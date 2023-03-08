import streamlit as st
from Assets.Sidebar import show_sidebar


st.set_page_config(page_title='F1 DataViz', page_icon=None, layout="wide", initial_sidebar_state="expanded", menu_items=None)
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Orbitron', sans-serif;
			}

            button {
                font-family: 'Helvetica', sans-serif !important;
                width: 100% !important;
            }
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.title('Formula One DataViz')
st.markdown("""<div style="text-align: justify">Check out my Streamlit App-a-Thon project, which provides fascinating insights into the F1 World Championship. 
The project offers a range of visualizations that display interesting information about the championship, such as the number of wins by each team, the position of drivers over time, and the 
distribution of lap times. You can explore the data using various types of charts, including bar charts, line charts, scatter plots, and radar charts. With this project, you'll gain a deeper 
understanding of the F1 World Championship and its history.</div>""", unsafe_allow_html=True)

show_sidebar()

