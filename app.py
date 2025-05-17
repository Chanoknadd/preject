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
    'Frequency [Lofi]': 'Q1',

    'Frequency [Pop]': 'Q2',
    'Frequency [K pop]': 'Q2',
    'Frequency [Latin]': 'Q2',
    'Frequency [R&B]': 'Q2',
    
    'Frequency [Hip hop]': 'Q3',
    'Frequency [Rap]': 'Q3',

    'Frequency [Rock]': 'Q4',
    'Frequency [Metal]': 'Q4',

    'Frequency [Country]': 'Q5',
    'Frequency [Folk]': 'Q5'
    'Frequency [Gospel]': 'Q5',

    'Frequency [EDM]': 'Q6',
    'Frequency [Video game music]': 'Q6',
    
}

# Streamlit UI
st.title("🎵 Favorite Music Genre Predictor")
st.write("Answer 6 questions about your listening habits (0 = Never, 4 = Very Often):")

# Add age input
age = st.number_input("Your age:", min_value=10, max_value=100, value=25, step=1)

# Frequency inputs (0-4 scale)
q1 = st.slider("1. How often do you listen to classical/relaxing music? (Classical, Jazz, Lofi)", 0, 4, 2)
q2 = st.slider("2. How often do you listen to pop or dance genres? (pop, k pop, latin, r&b)", 0, 4, 2)
q3 = st.slider("3. How often do you listen to hip hop or rap? (hip hop, rap)", 0, 4, 2)
q4 = st.slider("4. How often do you listen to rock, metal? (rock, metal)", 0, 4, 2)
q5 = st.slider("5. How often do you listen to acoustic/relaxing music? (country, folk, gospel)", 0, 4, 2)
q6 = st.slider("6. How often do you listen to electronic or game music? (EDM, Video game music)", 0, 4, 2)

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
