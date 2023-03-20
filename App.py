import streamlit as st
from Assets.Sidebar import show_sidebar
from _Pages import Nations, Main, Seasons


st.set_page_config(page_title='F1 DataViz', page_icon='🏎️', layout="wide", initial_sidebar_state="expanded", menu_items=None)
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Orbitron', sans-serif;
			}

            
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state['page'] = 'initial'
    Main.render_page()
elif st.session_state['page'] == 'nations':
    Nations.render_page()
elif st.session_state['page'] == 'seasons':
    Seasons.render_page()


show_sidebar()

