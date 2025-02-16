import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_excel("C:/Users/gcoat/Documents/texas-legislature-search/committees.xlsx")

st.title("Texas Legislature Committee Assignments Search")

search_term = st.text_input("Search for a Name or Committee:")

if search_term:
    results = df[df.apply(lambda row: search_term.lower() in row.to_string().lower(), axis=1)]
    if not results.empty:
        st.dataframe(results, width=800)  # Only show results if they exist
    else:
        st.write("No results found.")
else:
    st.write("Enter a search term above to find committee assignments.")
