import streamlit as st

st.title('Counter Example')

def main():

    if 'count' not in st.session_state:
        st.session_state.count = 0

    increment = st.button('Increment')
    if increment:
        st.session_state.count += 1

    st.write('Count = ', st.session_state.count)

if __name__ == '__main__':
    main()