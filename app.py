# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define genre-to-question mapping
genre_group_map = {
    'Frequency [Classical]': 'Q1',
    'Frequency [Jazz]': 'Q1',
    'Frequency [Folk]': 'Q1',
    'Frequency [Gospel]': 'Q1',

    'Frequency [Country]': 'Q2',
    'Frequency [Lofi]': 'Q2',

    'Frequency [EDM]': 'Q3',
    'Frequency [Video game music]': 'Q3',

    'Frequency [Hip hop]': 'Q4',
    'Frequency [Rap]': 'Q4',

    'Frequency [Pop]': 'Q5',
    'Frequency [K pop]': 'Q5',
    'Frequency [R&B]': 'Q5',

    'Frequency [Rock]': 'Q6',
    'Frequency [Metal]': 'Q6',
    'Frequency [Latin]': 'Q6'
}

# Create Streamlit UI
st.title("🎵 Favorite Music Genre Predictor (6 Questions)")
st.write("Answer the following to help us predict your favorite genre:")

# Ask 6 frequency questions
q1 = st.slider("1. How often do you listen to relaxing/classical genres (Classical, Jazz, Folk, Gospel)?", 0, 4, 2)
q2 = st.slider("2. How often do you listen to acoustic genres (Country, Lofi)?", 0, 4, 2)
q3 = st.slider("3. How often do you listen to electronic or gaming music (EDM, Video Game Music)?", 0, 4, 2)
q4 = st.slider("4. How often do you listen to hip hop/rap?", 0, 4, 2)
q5 = st.slider("5. How often do you listen to pop and dance genres (Pop, K-pop, R&B)?", 0, 4, 2)
q6 = st.slider("6. How often do you listen to rock, metal, or Latin music?", 0, 4, 2)

# Store answers
group_answers = {
    'Q1': q1,
    'Q2': q2,
    'Q3': q3,
    'Q4': q4,
    'Q5': q5,
    'Q6': q6
}

# Create feature dictionary
input_features = {}
for genre_feature, group_id in genre_group_map.items():
    input_features[genre_feature] = group_answers[group_id]

# Convert to DataFrame
input_df = pd.DataFrame([input_features])

# Predict
if st.button("🎧 Predict My Favorite Genre"):
    prediction = model.predict(input_df)
    st.success(f"Your predicted favorite genre is: **{prediction[0]}** 🎶")





