# -*- coding: utf-8 -*-
"""
Created on Wed May  7 00:34:05 2025

@author: Beam
"""

import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Mapping of each genre feature to one of the 6 questions
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

# Streamlit UI
st.title("🎵 Favorite Music Genre Predictor")
st.write("Answer 6 questions about your listening habits (0 = Never, 4 = Very Often):")

# Frequency inputs (0-4 scale)
q1 = st.slider("1. How often do you listen to classical/relaxing music? (Classical, Jazz, Folk, Gospel)", 0, 4, 2)
q2 = st.slider("2. How often do you listen to acoustic/lofi genres? (Country, Lofi)", 0, 4, 2)
q3 = st.slider("3. How often do you listen to electronic or game music? (EDM, Video game music)", 0, 4, 2)
q4 = st.slider("4. How often do you listen to hip hop or rap?", 0, 4, 2)
q5 = st.slider("5. How often do you listen to pop or dance genres? (Pop, K-pop, R&B)", 0, 4, 2)
q6 = st.slider("6. How often do you listen to rock, metal, or Latin music?", 0, 4, 2)

# Store answers by question ID
group_answers = {
    'Q1': q1,
    'Q2': q2,
    'Q3': q3,
    'Q4': q4,
    'Q5': q5,
    'Q6': q6
}

# Prepare input features mapped from 6 questions
input_features = {}
for genre_feature, group_id in genre_group_map.items():
    input_features[genre_feature] = group_answers[group_id]

# Ensure the DataFrame has all the correct columns in correct order
expected_features = model.feature_names_in_
input_df = pd.DataFrame([[input_features.get(feat, 0) for feat in expected_features]],
                        columns=expected_features)

# Prediction button
if st.button("🎧 Predict My Favorite Genre"):
    prediction = model.predict(input_df)
    st.success(f"Your predicted favorite genre is: **{prediction[0]}** 🎶")
