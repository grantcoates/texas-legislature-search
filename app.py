import os
import pandas as pd
import streamlit as st

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
        # Convert the filtered DataFrame to HTML with a custom CSS class
        html_table = results.to_html(classes="wrapped", index=False, escape=False)
        # Define CSS for the table: fixed layout and text wrapping
        css = """
        <style>
        table.wrapped {
            table-layout: fixed;
            width: 100%;
        }
        table.wrapped th, table.wrapped td {
            white-space: normal;
            word-wrap: break-word;
            overflow-wrap: break-word;
            padding: 8px;
            border: 1px solid #ddd;
        }
        </style>
        """
        # Display the HTML table with the CSS
        st.markdown(css + html_table, unsafe_allow_html=True)
    else:
        st.write("No results found.")
else:
    st.write("Enter a search term above to find committee assignments.")
