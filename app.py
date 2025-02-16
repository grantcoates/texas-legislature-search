import os
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

file_path = "committees.xlsx"  # Ensure this matches the GitHub filename

if os.path.exists(file_path):
    df = pd.read_excel(file_path)  # Uses relative path
else:
    st.error(f"❌ Error: The file '{file_path}' is missing. Check if it was uploaded correctly.")

st.title("Texas Legislature Committee Assignments Search")

search_term = st.text_input("Search for a Name, Committee, or Role:")

if search_term:
    # If the user types "chair" or "chairs", filter by Role
    if search_term.lower() in ["chair", "chairs"]:
        results = df[df['Role'].str.lower() == 'chair']
    else:
        results = df[df.apply(lambda row: search_term.lower() in row.to_string().lower(), axis=1)]
    
    if not results.empty:
        # Convert the DataFrame to an HTML table with a custom CSS class.
        html_table = results.to_html(classes="wrapped", index=False, escape=False)
        # Define custom CSS for the table.
        css = """
        <style>
        table.wrapped {
            table-layout: fixed;
            width: 100%;
        }
        table.wrapped th, table.wrapped td {
            white-space: pre-wrap;
            word-wrap: break-word;
            overflow-wrap: break-word;
            padding: 8px;
            border: 1px solid #ddd;
        }
        table.wrapped th {
            text-align: center;
            background-color: #f2f2f2; /* optional: change or remove */
        }
        </style>
        """
        # Render the HTML table with CSS using components.html.
        components.html(css + html_table, height=400, scrolling=True)
    else:
        st.write("No results found.")
else:
    st.write("Enter a search term above to find committee assignments.")
