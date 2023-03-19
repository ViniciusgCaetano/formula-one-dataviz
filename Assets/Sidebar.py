import streamlit as st



def show_sidebar():

    with st.sidebar:

        st.image("https://th.bing.com/th/id/R.b5420aeaf33a34e10dc5fa6d07874205?rik=zC58R62TClGl6w&pid=ImgRaw&r=0")
        if st.button('Nations', use_container_width=True):
            st.session_state['page'] = 'nations'
            st.experimental_rerun()
        st.button('Compare Drivers', use_container_width=True)
        st.button('Circuits', use_container_width=True)
        if st.button('Seasons', use_container_width=True):
            st.session_state['page'] = 'seasons'
            st.experimental_rerun()
