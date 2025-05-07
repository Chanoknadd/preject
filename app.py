# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load the trained model
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Label encoder for genre prediction
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
label_encoder.fit([
    'Classical', 'Country', 'EDM', 'Folk', 'Gospel', 'Hip hop', 'Jazz',
    'K pop', 'Latin', 'Lofi', 'Metal', 'Pop', 'R&B', 'Rap', 'Rock', 'Video game music'
])

# Frequency mapping
frequency_map = {'Never': 0, 'Sometimes': 1, 'Often': 2}

# Cluster mapping function (for display, not needed in prediction)
def map_cluster(frequencies):
    # Dummy function if needed to determine cluster
    return 1  # Placeholder

# Streamlit UI
st.title("🎵 Predict Your Favorite Music Genre")
st.write("Answer the questions below to predict your favorite music genre!")

# User input
age = st.slider("What's your age?", min_value=10, max_value=80, value=25)

q1 = st.selectbox("How often do you enjoy calming, instrumental, or sophisticated sounds (Classical, Jazz, Lofi)?", ['Never', 'Sometimes', 'Often'])
q2 = st.selectbox("How often do you enjoy heartfelt lyrics, acoustic sounds, or music rooted in storytelling (Country, Folk, Gospel)?", ['Never', 'Sometimes', 'Often'])
q3 = st.selectbox("How often do you enjoy high-energy, electronic music or immersive background game music (EDM, Video Game Music)?", ['Never', 'Sometimes', 'Often'])
q4 = st.selectbox("How often do you enjoy energetic beats and clever lyrics (Hip-Hop, Rap)?", ['Never', 'Sometimes', 'Often'])
q5 = st.selectbox("How often do you sing along to catchy, chart-topping songs or dance to smooth beats (Pop, R&B, K-Pop, Latin)?", ['Never', 'Sometimes', 'Often'])
q6 = st.selectbox("How often do you listen to guitar-heavy tracks, loud drums, or rock anthems (Rock, Metal)?", ['Never', 'Sometimes', 'Often'])

# Map user answers to each genre
input_dict = {
    'Age': age,
    'Frequency [Classical]': frequency_map[q1],
    'Frequency [Jazz]': frequency_map[q1],
    'Frequency [Lofi]': frequency_map[q1],
    'Frequency [Country]': frequency_map[q2],
    'Frequency [Folk]': frequency_map[q2],
    'Frequency [Gospel]': frequency_map[q2],
    'Frequency [EDM]': frequency_map[q3],
    'Frequency [Video game music]': frequency_map[q3],
    'Frequency [Hip hop]': frequency_map[q4],
    'Frequency [Rap]': frequency_map[q4],
    'Frequency [Pop]': frequency_map[q5],
    'Frequency [R&B]': frequency_map[q5],
    'Frequency [K pop]': frequency_map[q5],
    'Frequency [Latin]': frequency_map[q5],
    'Frequency [Rock]': frequency_map[q6],
    'Frequency [Metal]': frequency_map[q6],
    'Cluster Group': 0  # Can update this if used
}

# Reorder and fill missing genre frequencies with 0 if not in input_dict
expected_features = [
    'Age', 'Frequency [Classical]', 'Frequency [Country]', 'Frequency [EDM]',
    'Frequency [Folk]', 'Frequency [Gospel]', 'Frequency [Hip hop]', 'Frequency [Jazz]',
    'Frequency [K pop]', 'Frequency [Latin]', 'Frequency [Lofi]', 'Frequency [Metal]',
    'Frequency [Pop]', 'Frequency [R&B]', 'Frequency [Rap]', 'Frequency [Rock]',
    'Frequency [Video game music]', 'Cluster Group']

# Fill missing with 0
for feat in expected_features:
    if feat not in input_dict:
        input_dict[feat] = 0

# Create input array for prediction
input_data = pd.DataFrame([input_dict])[expected_features]

# Predict
if st.button("Predict Genre"):
    predicted_label = model.predict(input_data)[0]
    predicted_genre = label_encoder.inverse_transform([predicted_label])[0]
    st.success(f"🎧 Your predicted favorite genre is: **{predicted_genre}**")



