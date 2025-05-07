# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Use the correct feature order that was used during model training
expected_features = [
    'Age',
    'Frequency [Classical]',
    'Frequency [Country]',
    'Frequency [EDM]',
    'Frequency [Folk]',
    'Frequency [Gospel]',
    'Frequency [Hip hop]',
    'Frequency [Jazz]',
    'Frequency [K pop]',
    'Frequency [Latin]',
    'Frequency [Lofi]',
    'Frequency [Metal]',
    'Frequency [Pop]',
    'Frequency [R&B]',
    'Frequency [Rap]',
    'Frequency [Rock]',
    'Frequency [Video game music]',
    'Cluster Group'
]

frequency_map = {'Never': 0, 'Sometimes': 1, 'Often': 2}

genre_questions = {
    "Classical/Jazz/Lofi": ["Frequency [Classical]", "Frequency [Jazz]", "Frequency [Lofi]"],
    "Pop/R&B/K-Pop/Latin": ["Frequency [Pop]", "Frequency [R&B]", "Frequency [K pop]", "Frequency [Latin]"],
    "Hip-Hop/Rap": ["Frequency [Hip hop]", "Frequency [Rap]"],
    "Rock/Metal": ["Frequency [Rock]", "Frequency [Metal]"],
    "Country/Folk/Gospel": ["Frequency [Country]", "Frequency [Folk]", "Frequency [Gospel]"],
    "EDM/Video Game Music": ["Frequency [EDM]", "Frequency [Video game music]"]
}

cluster_map = {
    "Classical/Jazz/Lofi": 1,
    "Pop/R&B/K-Pop/Latin": 2,
    "Hip-Hop/Rap": 3,
    "Rock/Metal": 4,
    "Country/Folk/Gospel": 5,
    "EDM/Video Game Music": 6
}

st.title("🎧 Predict Your Favorite Music Genre")

age = st.slider("What is your age?", 10, 80, 25)

frequencies = {}
cluster_group = None

for group, genres in genre_questions.items():
    response = st.selectbox(
        f"How often do you listen to {group} music?",
        options=frequency_map.keys(),
        key=group
    )
    value = frequency_map[response]
    for g in genres:
        frequencies[g] = value
    if cluster_group is None or value > 0:
        cluster_group = cluster_map[group]

# Prepare input
input_data = {
    'Age': age,
    'Cluster Group': cluster_group
}
for feature in expected_features:
    if feature.startswith("Frequency"):
        input_data[feature] = frequencies.get(feature, 0)

# Reorder to match expected model input
input_df = pd.DataFrame([input_data])[expected_features]

# Predict
if st.button("Predict Favorite Genre"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🎵 Your predicted favorite genre label is: **{prediction}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")




