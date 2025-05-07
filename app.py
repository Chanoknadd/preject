# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model and label encoder
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the genre clusters
def map_to_cluster(fav_genres):
    fav_genres = [g.lower() for g in fav_genres]
    if any(g in ['classical', 'jazz', 'lofi'] for g in fav_genres):
        return 1
    elif any(g in ['pop', 'k pop', 'latin', 'r&b'] for g in fav_genres):
        return 2
    elif any(g in ['hip hop', 'rap'] for g in fav_genres):
        return 3
    elif any(g in ['rock', 'metal'] for g in fav_genres):
        return 4
    elif any(g in ['country', 'folk', 'gospel'] for g in fav_genres):
        return 5
    elif any(g in ['edm', 'video game music'] for g in fav_genres):
        return 6
    else:
        return 0  # default or unknown

# Feature list
features = [
    'Age', 'Frequency [Classical]', 'Frequency [Country]', 'Frequency [EDM]',
    'Frequency [Folk]', 'Frequency [Gospel]', 'Frequency [Hip hop]',
    'Frequency [Jazz]', 'Frequency [K pop]', 'Frequency [Latin]',
    'Frequency [Lofi]', 'Frequency [Metal]', 'Frequency [Pop]', 'Frequency [R&B]',
    'Frequency [Rap]', 'Frequency [Rock]', 'Frequency [Video game music]',
    'Cluster Group'
]

# Frequency map
frequency_map = {
    'Never': 0,
    'Sometimes': 1,
    'Often': 2
}


# Streamlit UI
st.title("🎵 Music Genre Prediction")
st.write("Answer the questions below to get your predicted favorite music genre.")

age = st.slider("Your age:", 10, 80, 25)

st.subheader("🎶 How often do you listen to...")
freq_classical = frequency_map[st.selectbox("Classical / Jazz / Lofi", list(frequency_map.keys()))]
freq_pop = frequency_map[st.selectbox("Pop / R&B / K-pop / Latin", list(frequency_map.keys()))]
freq_hiphop = frequency_map[st.selectbox("Hip-Hop / Rap", list(frequency_map.keys()))]
freq_rock = frequency_map[st.selectbox("Rock / Metal", list(frequency_map.keys()))]
freq_country = frequency_map[st.selectbox("Country / Folk / Gospel", list(frequency_map.keys()))]
freq_edm = frequency_map[st.selectbox("EDM / Video Game Music", list(frequency_map.keys()))]

st.subheader("🎧 Background info")
while_working = binary_map[st.radio("Do you listen to music while working?", list(binary_map.keys()))]
instrumentalist = binary_map[st.radio("Are you an instrumentalist?", list(binary_map.keys()))]
composer = binary_map[st.radio("Do you compose music?", list(binary_map.keys()))]
foreign_languages = binary_map[st.radio("Do you speak foreign languages?", list(binary_map.keys()))]

# Generate full feature vector
input_data = pd.DataFrame([[
    age,
    freq_classical, freq_country, freq_edm,
    freq_country, freq_country, freq_hiphop,
    freq_classical, freq_pop, freq_pop,
    freq_classical, freq_rock, freq_pop, freq_pop,
    freq_hiphop, freq_rock, freq_edm,
    while_working, instrumentalist, composer, foreign_languages,
    hours,
    map_to_cluster(['Classical' if freq_classical > 0 else '',
                    'Pop' if freq_pop > 0 else '',
                    'Hip hop' if freq_hiphop > 0 else '',
                    'Rock' if freq_rock > 0 else '',
                    'Country' if freq_country > 0 else '',
                    'EDM' if freq_edm > 0 else ''])
]], columns=features)

if st.button("Predict Favorite Genre"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🎵 Your predicted favorite genre label is: {prediction}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")



