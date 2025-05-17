# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import streamlit as st
import pandas as pd
import pickle

# Load the trained RandomForest model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# List of music genres used as features
genre_features = [
    'Pop', 'Rock', 'HipHop', 'Jazz', 'Classical', 'Country',
    'Electronic', 'R&B', 'Reggae', 'Blues', 'Metal', 'Folk',
    'Soul', 'Latin', 'Punk', 'EDM'
]

st.title("🎶 Music Genre Predictor")
st.write("Rate how often you listen to each genre (0 = Never, 4 = Very Often):")

# Collect frequency input for each genre
user_input = {}
for genre in genre_features:
    user_input[genre] = st.slider(f"{genre}", 0, 4, 2)

# Convert input into DataFrame
input_df = pd.DataFrame([user_input])

# Predict button
if st.button("🎧 Predict My Favorite Genre"):
    prediction = model.predict(input_df)
    st.success(f"Your predicted favorite genre is: **{prediction[0]}** 🎵")





