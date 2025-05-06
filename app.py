# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import pickle
import pandas as pd

# Load trained model
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Frequency mapping
frequency_map = {
    'Never': 0,
    'Sometimes': 1,
    'Often': 2
}

# User input grouped by genre clusters
user_answers = {
    'Pop/R&B/K-Pop/Latin': 'Often',
    'Hip-Hop/Rap': 'Often',
    'Rock/Metal': 'Never',
    'Classical/Jazz/Lofi': 'Sometimes',
    'Country/Folk/Gospel': 'Sometimes',
    'EDM/Video Game Music': 'Often'
}

# Mapping from group to individual genres
group_to_genres = {
    'Classical/Jazz/Lofi': ['Frequency [Classical]', 'Frequency [Jazz]', 'Frequency [Lofi]'],
    'Pop/R&B/K-Pop/Latin': ['Frequency [Pop]', 'Frequency [R&B]', 'Frequency [K pop]', 'Frequency [Latin]'],
    'Hip-Hop/Rap': ['Frequency [Hip hop]', 'Frequency [Rap]'],
    'Rock/Metal': ['Frequency [Rock]', 'Frequency [Metal]'],
    'Country/Folk/Gospel': ['Frequency [Country]', 'Frequency [Folk]', 'Frequency [Gospel]'],
    'EDM/Video Game Music': ['Frequency [EDM]', 'Frequency [Video game music]']
}

# Construct full feature input for the model
user_input_full = {}

# Spread the group frequency to each genre feature
for group, answer in user_answers.items():
    value = frequency_map[answer]
    for genre_feature in group_to_genres[group]:
        user_input_full[genre_feature] = value

# Add other features your model requires with default/sample values
user_input_full.update({
    'Hours per day': 2,
    'While working': 1,
    'Instrumentalist': 0,
    'Composer': 0,
    'Foreign languages': 1
})

# Create DataFrame in the right column order
input_df = pd.DataFrame([user_input_full])

# Add any missing columns with 0 (if needed)
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0

# Reorder columns to match model input
input_df = input_df[model.feature_names_in_]

# Make prediction
predicted_label = model.predict(input_df)[0]


# Show result
print(f"Predicted favorite genre: {predicted_genre}")

