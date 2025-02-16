import os
import pandas as pd
import streamlit as st

file_path = "committees.xlsx"  # Ensure this matches the GitHub filename

if os.path.exists(file_path):
    df = pd.read_excel(file_path)  # Uses relative path
else:
    st.error(f"❌ Error: The file '{file_path}' is missing. Check if it was uploaded correctly.")

# Streamlit app setup
st.title("Texas Legislature Committee Assignments Search")

# Search function
search_term = st.text_input("Search for a Name or Committee:")

if search_term:
    results = df[df.apply(lambda row: search_term.lower() in row.to_string().lower(), axis=1)]
    if not results.empty:
        st.dataframe(results, use_container_width=True)  # Keeps column formatting & allows scrolling
    else:
        st.write("No results found.")
else:
    st.write("Enter a search term above to find committee assignments.")

