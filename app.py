# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define frequency mapping
frequency_map = {
    'Never': 0,
    'Sometimes': 1,
    'Often': 2
}

# Define genre groups and related genres
genre_questions = {
    "Classical/Jazz/Lofi": ["Frequency [Classical]", "Frequency [Jazz]", "Frequency [Lofi]"],
    "Pop/R&B/K-Pop/Latin": ["Frequency [Pop]", "Frequency [R&B]", "Frequency [K pop]", "Frequency [Latin]"],
    "Hip-Hop/Rap": ["Frequency [Hip hop]", "Frequency [Rap]"],
    "Rock/Metal": ["Frequency [Rock]", "Frequency [Metal]"],
    "Country/Folk/Gospel": ["Frequency [Country]", "Frequency [Folk]", "Frequency [Gospel]"],
    "EDM/Video Game Music": ["Frequency [EDM]", "Frequency [Video game music]"]
}

# Map group to cluster ID
cluster_map = {
    "Classical/Jazz/Lofi": 1,
    "Pop/R&B/K-Pop/Latin": 2,
    "Hip-Hop/Rap": 3,
    "Rock/Metal": 4,
    "Country/Folk/Gospel": 5,
    "EDM/Video Game Music": 6
}

st.title("🎧 Music Genre Predictor")

# User input: Age
age = st.slider("What is your age?", 10, 80, 25)

# Get frequency input for each group
frequencies = {}
cluster_group = None
for group, genres in genre_questions.items():
    answer = st.selectbox(
        f"How often do you listen to {group} music?",
        options=list(frequency_map.keys()),
        key=group
    )
    freq_value = frequency_map[answer]
    for genre in genres:
        frequencies[genre] = freq_value
    if cluster_group is None or freq_value > 0:
        cluster_group = cluster_map[group]

# Prepare input data
input_features = {
    'Age': age,
    'Frequency [Classical]': frequencies.get('Frequency [Classical]', 0),
    'Frequency [Country]': frequencies.get('Frequency [Country]', 0),
    'Frequency [EDM]': frequencies.get('Frequency [EDM]', 0),
    'Frequency [Folk]': frequencies.get('Frequency [Folk]', 0),
    'Frequency [Gospel]': frequencies.get('Frequency [Gospel]', 0),
    'Frequency [Hip hop]': frequencies.get('Frequency [Hip hop]', 0),
    'Frequency [Jazz]': frequencies.get('Frequency [Jazz]', 0),
    'Frequency [K pop]': frequencies.get('Frequency [K pop]', 0),
    'Frequency [Latin]': frequencies.get('Frequency [Latin]', 0),
    'Frequency [Lofi]': frequencies.get('Frequency [Lofi]', 0),
    'Frequency [Metal]': frequencies.get('Frequency [Metal]', 0),
    'Frequency [Pop]': frequencies.get('Frequency [Pop]', 0),
    'Frequency [R&B]': frequencies.get('Frequency [R&B]', 0),
    'Frequency [Rap]': frequencies.get('Frequency [Rap]', 0),
    'Frequency [Rock]': frequencies.get('Frequency [Rock]', 0),
    'Frequency [Video game music]': frequencies.get('Frequency [Video game music]', 0),
    'Cluster Group': cluster_group
}

# Convert to DataFrame
input_df = pd.DataFrame([input_features])

# Prediction
if st.button("Predict Favorite Genre"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🎵 Your predicted favorite genre is: **{prediction}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")




