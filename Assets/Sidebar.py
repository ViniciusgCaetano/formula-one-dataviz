import streamlit as st



def show_sidebar():

    with st.sidebar:

        st.image("https://raw.githubusercontent.com/ViniciusgCaetano/formula-one-dataviz/master/images/fonedataviz.png")
        st.title(" \n \n ")
        if st.button('Nations', use_container_width=True):
            st.session_state['page'] = 'nations'
            st.experimental_rerun()
        st.button('Compare Drivers', use_container_width=True)
        st.button('Circuits', use_container_width=True)
        if st.button('Seasons', use_container_width=True):
            st.session_state['page'] = 'seasons'
            st.experimental_rerun()
