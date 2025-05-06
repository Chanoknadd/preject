# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

#import library
import streamlit as st
import pickle

# Load trained model
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Map text answers to numeric frequency
frequency_map = {
    'Never': 0,
    'Rarely': 1,
    'Often': 2,
}

# Define 3 questions (sample)
questions = {
    'Pop/R&B/K-Pop/Latin': "🎶 How often do you enjoy catchy, danceable songs or global pop hits?",
    'Hip-Hop/Rap': "🎤 Do you listen to energetic beats or powerful rap verses?",
    'Classical/Jazz/Lofi': "🎻 Do you prefer calming, instrumental, or relaxing music like classical or lofi?"
}

st.title("🎵 Music Taste Predictor (Sample)")

st.write("Answer these 3 questions and get a predicted music cluster group!")

user_input = []

# Ask each question
for genre_group, question in questions.items():
    answer = st.selectbox(question, ['Never', 'Sometimes', 'Often'], key=genre_group)
    user_input.append(frequency_map[answer])

# Predict button
if st.button("Predict Cluster"):
    prediction = model.predict([user_input])[0]
    st.success(f"✅ You belong to **Cluster {prediction}**")

    # Optional: Show cluster meaning
    cluster_descriptions = {
        '1': "Classical / Jazz / Lofi 🎷",
        '2': "Pop / R&B / K-Pop / Latin 🎤",
        '3': "Hip-Hop / Rap 🔥",
        '4': "Rock / Metal 🎸",
        '5': "Country / Folk / Gospel 🎻",
        '6': "EDM / Video Game Music 🎮"
    }
    st.write(f"🎧 Genre group: {cluster_descriptions.get(str(prediction), 'Unknown')}")
