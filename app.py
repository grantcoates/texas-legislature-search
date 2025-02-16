import os
import pandas as pd
import streamlit as st

# Updated CSS: fixed table layout with explicit column widths
st.markdown(
    """
    <style>
    .stDataFrame table {
        table-layout: fixed;
        width: 100%;
    }
    .stDataFrame table tr th,
    .stDataFrame table tr td {
        white-space: pre-wrap;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    /* Set the first column ("Name") to 25% of the table width */
    .stDataFrame table tr th:nth-child(1),
    .stDataFrame table tr td:nth-child(1) {
        width: 25%;
    }
    /* Set the second column ("Committee") to 75% of the table width */
    .stDataFrame table tr th:nth-child(2),
    .stDataFrame table tr td:nth-child(2) {
        width: 75%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

file_path = "committees.xlsx"  # Ensure this matches the GitHub filename

if os.path.exists(file_path):
    df = pd.read_excel(file_path)  # Uses relative path
else:
    st.error(f"❌ Error: The file '{file_path}' is missing. Check if it was uploaded correctly.")

st.title("Texas Legislature Committee Assignments Search")

search_term = st.text_input("Search for a Name, Committee, or Role:")

if search_term:
    # If user types "chair" or "chairs", filter by Role; otherwise, do a general search.
    if search_term.lower() in ["chair", "chairs"]:
        results = df[df['Role'].str.lower() == 'chair']
    else:
        results = df[df.apply(lambda row: search_term.lower() in row.to_string().lower(), axis=1)]
    
    if not results.empty:
        st.dataframe(results, use_container_width=True)
    else:
        st.write("No results found.")
else:
    st.write("Enter a search term above to find committee assignments.")
