import streamlit as st
import os

st.title('Embedding UI')


if os.path.exists('options/list.txt'):
    with open('options/list.txt', 'r') as f:
        initial_options = [line.strip() for line in f.readlines() if line.strip()]
        saved_options = []
        for option in initial_options:
            if option not in saved_options:
                saved_options.append(option)
else:
    saved_options = []

if "selected_options" not in st.session_state:
    st.session_state.selected_options = []



# Upload Documents
uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file.seek(0)
        st.write(file.read())  

add_options = st.text_input('Add options')
saved_options.append(add_options)

st.session_state.selected_options = st.multiselect('Select', saved_options)


with open('options/list.txt', 'w') as f:
    for option in saved_options:
        f.write(option + '\n')

