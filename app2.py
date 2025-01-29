# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:52:03 2025

@author: T480
"""

import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

st.image("C:\Users\T480\streamlit")

# Collect basic information
name = "Basheerah Sulliman"
field = "Chemistry"
institution = "University of The Western Cape"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")
        
st.title("About Me")
st.write("As an honours student passionate about pushing the boundaries of scientific discovery, I am deeply invested in the fascinating field of computational chemistry. My academic journey has led me to explore the intricate interplay between molecular structures and computational methods, fueling my desire to contribute to innovative research that bridges theoretical knowledge with practical applications. With a keen interest in leveraging advanced computational techniques to solve complex chemical problems, I am eager to delve into research that not only expands our understanding of chemical phenomena but also paves the way for groundbreaking advancements in various industries. My commitment to excellence, coupled with a relentless curiosity, drives me to continuously seek new challenges and opportunities for growth within the realm of computational chemistry.")
st.link_button("my LinkedIn", "https://za.linkedin.com/in/basheerah-sulliman-76343a307")


# Add a contact section
st.header("Contact Information")
email = "4282193@myuwc.ac.za"
st.write(f"You can reach {name} at {email}.")


