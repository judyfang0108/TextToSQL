import streamlit as st
from utils import *

st.set_page_config(page_title="Database Q/A App", page_icon=":bookmark_tabs:")

# st.image("logo.jpg",width=100)
st.title('SQL Database :red[Q/A App] 	:open_book:')

# Sidebar for model selection
model_choice = st.sidebar.selectbox(
    "Choose a Language Model:",
    ("Google Gemini", "ChatGPT-4o")
)


question = st.text_input(":violet[Question: ]")
# Submit button
submit = st.button("Submit")

if question and submit:
    # Get the SQL agent executor
    chain = get_db_chain(model_choice)

    # Execute the query and get the response
    with st.spinner("Processing your query..."):
        response = execute_query(question, model_choice)

    # Display the response
    st.header("Answer")
    if isinstance(response, str):
        st.write(response)
    else:
        st.dataframe(response)