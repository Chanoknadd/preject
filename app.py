# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load trained model
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Recreate label encoder with same classes used during training
label_encoder = LabelEncoder()
label_encoder.fit([
    'Classical', 'Country', 'EDM', 'Folk', 'Gospel', 'Hip hop', 'Jazz',
    'K pop', 'Latin', 'Lofi', 'Metal', 'Pop', 'R&B', 'Rap', 'Rock', 'Video game music'
])

# Frequency mapping
frequency_map = {'Never': 0, 'Sometimes': 1, 'Often': 2}

# Streamlit UI
st.title("🎵 Music Genre Predictor")
st.write("Answer the following questions to find your predicted favorite music genre!")

# Questions (6 groups)
q1 = st.selectbox("1. How often do you listen to catchy, chart-topping songs (Pop, R&B, K-Pop, Latin)?",
                  ['Never', 'Sometimes', 'Often'])

q2 = st.selectbox("2. Do you enjoy energetic beats and clever lyrics (Hip-Hop, Rap)?",
                  ['Never', 'Sometimes', 'Often'])

q3 = st.selectbox("3. Do you love guitar-heavy tracks, loud drums, or headbanging rock anthems (Rock, Metal)?",
                  ['Never', 'Sometimes', 'Often'])

q4 = st.selectbox("4. Do you prefer calming, instrumental, or sophisticated sounds (Classical, Jazz, Lofi)?",
                  ['Never', 'Sometimes', 'Often'])

q5 = st.selectbox("5. How often do you enjoy heartfelt lyrics, acoustic sounds (Country, Folk, Gospel)?",
                  ['Never', 'Sometimes', 'Often'])

q6 = st.selectbox("6. Do you love high-energy, electronic music or video game music (EDM, Video Game Music)?",
                  ['Never', 'Sometimes', 'Often'])

# Prediction button
if st.button("Predict Favorite Genre"):
    # Prepare user input in the correct feature order used in training
    input_data = np.array([
        frequency_map[q1],  # Group 2
        frequency_map[q2],  # Group 3
        frequency_map[q3],  # Group 4
        frequency_map[q4],  # Group 1
        frequency_map[q5],  # Group 5
        frequency_map[q6],  # Group 6
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  # Placeholder values for other features
    ]).reshape(1, -1)  # Adjust depending on model input size

    # Predict
    predicted_label = model.predict(input_data)[0]
    predicted_genre = label_encoder.inverse_transform([predicted_label])[0]

    # Show result
    st.success(f"🎧 Your predicted favorite music genre is: **{predicted_genre}**")



