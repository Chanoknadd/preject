# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load model
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load LabelEncoder
label_encoder = LabelEncoder()
label_encoder.classes_ = [
    'Classical', 'Country', 'EDM', 'Folk', 'Gospel', 'Hip hop', 'Jazz',
    'K pop', 'Latin', 'Lofi', 'Metal', 'Pop', 'R&B', 'Rap', 'Rock', 'Video game music'
]

# Frequency map
frequency_map = {
    'Never': 0,
    'Sometimes': 1,
    'Often': 2
}

# Streamlit app
st.title("🎵 Favorite Genre Predictor")

st.write("Answer the following questions to find out your predicted favorite music genre.")

# User questions (sample: 3 groups)
pop_response = st.selectbox("How often do you listen to catchy, danceable songs (Pop, R&B, K-Pop, Latin)?",
                            options=['Never', 'Sometimes', 'Often'])

hiphop_response = st.selectbox("Do you enjoy energetic beats and powerful lyrics (Hip-Hop, Rap)?",
                               options=['Never', 'Sometimes', 'Often'])

classical_response = st.selectbox("Do you like calming, instrumental music (Classical, Jazz, Lofi)?",
                                  options=['Never', 'Sometimes', 'Often'])

# Convert responses to values
user_answers = {
    'Pop/R&B/K-Pop/Latin': pop_response,
    'Hip-Hop/Rap': hiphop_response,
    'Classical/Jazz/Lofi': classical_response
}

group_to_genres = {
    'Pop/R&B/K-Pop/Latin': ['Frequency [Pop]', 'Frequency [R&B]', 'Frequency [K pop]', 'Frequency [Latin]'],
    'Hip-Hop/Rap': ['Frequency [Hip hop]', 'Frequency [Rap]'],
    'Classical/Jazz/Lofi': ['Frequency [Classical]', 'Frequency [Jazz]', 'Frequency [Lofi]'],
}

# Submit button
if st.button("Predict"):
    user_input_full = {}

    # Map frequency to genre features
    for group, answer in user_answers.items():
        value = frequency_map[answer]
        for genre_feature in group_to_genres[group]:
            user_input_full[genre_feature] = value

    # Add dummy/default values for required features
    user_input_full.update({
        'Hours per day': 2,
        'While working': 1,
        'Instrumentalist': 0,
        'Composer': 0,
        'Foreign languages': 1,
        # Fill missing genre features with 0
        'Frequency [Rock]': 0,
        'Frequency [Metal]': 0,
        'Frequency [Country]': 0,
        'Frequency [Folk]': 0,
        'Frequency [Gospel]': 0,
        'Frequency [EDM]': 0,
        'Frequency [Video game music]': 0
    })

    # Prepare input dataframe
    input_df = pd.DataFrame([user_input_full])
    for col in model.feature_names_in_:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[model.feature_names_in_]

    # Predict
    predicted_label = model.predict(input_df)[0]
    predicted_genre = label_encoder.inverse_transform([predicted_label])[0]

    st.success(f"🎧 Your predicted favorite genre is: **{predicted_genre}**")


