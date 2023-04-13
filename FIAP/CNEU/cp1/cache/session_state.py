import streamlit as st

def init_session_state():
    if 'form' not in st.session_state:
        st.session_state.form = None