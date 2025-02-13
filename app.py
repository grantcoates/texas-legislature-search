import streamlit as st
import pandas as pd

# Load the data
data = [
    ["Agriculture & Livestock", "Guillen, Ryan", "Chair"],
    ["Agriculture & Livestock", "Guerra, R.D. 'Bobby'", "Vice-Chair"],
    ["Agriculture & Livestock", "Kitzman, Stan", "Seniority Appointment"],
    ["Agriculture & Livestock", "Lopez, Janie of Cameron", "Seniority Appointment"],
    ["Agriculture & Livestock", "McLaughlin, Don", "Seniority Appointment"],
    ["Agriculture & Livestock", "Cain, Briscoe", "Speaker Appointment"],
    ["Agriculture & Livestock", "Hopper, Andy", "Speaker Appointment"],
    ["Agriculture & Livestock", "Money, Brent", "Speaker Appointment"],
    ["Agriculture & Livestock", "Muñoz, Sergio Jr.", "Speaker Appointment"],
    
    ["Appropriations", "Bonnen, Greg", "Chair"],
    ["Appropriations", "González, Mary of El Paso", "Vice-Chair"],
    ["Appropriations", "Bonnen, Greg", "Seniority Appointment"],
    ["Appropriations", "Collier, Nicole", "Seniority Appointment"],
    ["Appropriations", "Gervin-Hawkins, Barbara", "Seniority Appointment"],
    ["Appropriations", "Goodwin, Vikki", "Seniority Appointment"],
    ["Appropriations", "Harrison, Brian", "Seniority Appointment"],
    ["Appropriations", "Howard, Donna", "Seniority Appointment"],
    ["Appropriations", "Lozano, J. M.", "Seniority Appointment"],
    ["Appropriations", "Martinez, Armando", "Seniority Appointment"],
    ["Appropriations", "Oliverson, Tom", "Seniority Appointment"],
    ["Appropriations", "Rose, Toni", "Seniority Appointment"],
    ["Appropriations", "Slawson, Shelby", "Seniority Appointment"],
    ["Appropriations", "Wu, Gene", "Seniority Appointment"],
    ["Appropriations", "Barry, Jeff", "Speaker Appointment"],
    ["Appropriations", "DeAyala, Mano", "Speaker Appointment"],
    ["Appropriations", "Fairly, Caroline", "Speaker Appointment"],
    ["Appropriations", "Garcia Hernandez, Cassandra", "Speaker Appointment"],
    ["Appropriations", "Jones, Venton of Dallas", "Speaker Appointment"],
    ["Appropriations", "Kitzman, Stan", "Speaker Appointment"],
    ["Appropriations", "Lopez, Janie of Cameron", "Speaker Appointment"],
    ["Appropriations", "Lujan, John", "Speaker Appointment"],
    ["Appropriations", "Manuel, Christian", "Speaker Appointment"],
    ["Appropriations", "Orr, Angelia", "Speaker Appointment"],
    ["Appropriations", "Simmons, Lauren A.", "Speaker Appointment"],
    ["Appropriations", "Tepper, Carl", "Speaker Appointment"],
    ["Appropriations", "Villalobos, Denise", "Speaker Appointment"],
    ["Appropriations", "Walle, Armando", "Speaker Appointment"],
]

# Convert into DataFrame
df = pd.DataFrame(data, columns=["Committee", "Member", "Role"])

# Streamlit app setup
st.title("Texas Legislature Committee Assignments Search")

search_term = st.text_input("Search for a Name or Committee:")

if search_term:
    results = df[df.apply(lambda row: search_term.lower() in row.to_string().lower(), axis=1)]
    if not results.empty:
        st.write(results)
    else:
        st.write("No results found.")
else:
    st.write("Enter a search term above to find committee assignments.")
