import streamlit as st



def show_sidebar():

    with st.sidebar:

        st.image("https://raw.githubusercontent.com/ViniciusgCaetano/formula-one-dataviz/master/images/fonedataviz.png")
        st.title(" \n \n ")
        if st.button('Nations', use_container_width=True):
            st.session_state['page'] = 'nations'
            st.experimental_rerun()
      
        if st.button('Seasons', use_container_width=True):
            st.session_state['page'] = 'seasons'
            st.experimental_rerun()
