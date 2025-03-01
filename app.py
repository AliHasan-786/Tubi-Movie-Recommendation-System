# -*- coding: utf-8 -*-
"""App

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MEMvL6nHcgeVgUY0MjcLcgo7KTKbMEjD
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import streamlit as st
import openai
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load Data
df = pd.read_csv('Tubi_with_Personas_and_Clusters.csv')

# Combined Features for TF-IDF
df['Combined_Features'] = df.apply(lambda row: f"{row['Movie Genre']} {row['Movie Rating']} {row['Movie Length (Minutes)']}", axis=1)

# Vectorization and Similarity
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['Combined_Features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Persona Boost Weight
PERSONA_BOOST = 0.2
title_to_index = pd.Series(df.index, index=df['Title']).to_dict()

# Recommendation Logic
def get_recommendations(movie_title, top_n=5):
    if movie_title not in title_to_index:
        return [], None, None, None, None

    idx = title_to_index[movie_title]
    target_persona = df.iloc[idx]['Persona']
    target_cluster = df.iloc[idx]['Cluster']
    target_genres = df.iloc[idx]['Movie Genre'].split('·')
    target_length = df.iloc[idx]['Movie Length (Minutes)']

    sim_scores = list(enumerate(cosine_sim[idx]))

    boosted_scores = []
    for i, score in sim_scores:
        if i == idx:
            continue
        persona_bonus = PERSONA_BOOST if df.iloc[i]['Persona'] == target_persona else 0
        boosted_score = score + persona_bonus
        boosted_scores.append((i, boosted_score))

    boosted_scores = sorted(boosted_scores, key=lambda x: x[1], reverse=True)

    recommendations = [df.iloc[i]['Title'] for i, score in boosted_scores[:top_n]]

    return recommendations, target_persona, target_cluster, target_genres, target_length

# LLM Explanation Generator
def generate_explanation(movie_title, persona, cluster, genres, length):
    prompt = f"""
    You are a helpful movie recommendation assistant for Tubi.
    The user just watched "{movie_title}", and we generated 5 recommendations based on their preferences.
    Here are the user's attributes:
    - Persona: {persona}
    - Cluster Group: {cluster}
    - Preferred Genres: {', '.join(genres)}
    - Average Preferred Movie Length: {length:.0f} minutes

    Please generate a friendly, conversational explanation (2-3 sentences) that explains why these movies were recommended.
    Keep it casual but insightful.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a fun, helpful movie recommendation explainer for Tubi."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# Load OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit UI
st.title("🎥 Tubi Movie Recommender + AI Explanation")
st.write("Hybrid Recommendation Engine with Persona Boost + LLM Explanation")

sample_movies = df['Title'].sample(20, random_state=42).tolist()
st.write("🔎 Choose a movie you like to get started. Here are some examples you can pick from:")
st.write(", ".join(sample_movies))

movie_choice = st.selectbox("Select a Movie You Like:", df['Title'].unique())

if st.button("Get Recommendations"):
    recommendations, persona, cluster, genres, avg_length = get_recommendations(movie_choice)

    if recommendations:
        st.success(f"Top Recommendations for '{movie_choice}':")
        for idx, rec in enumerate(recommendations, start=1):
            st.write(f"{idx}. {rec}")

        explanation = generate_explanation(
            movie_title=movie_choice,
            persona=persona,
            cluster=cluster,
            genres=genres,
            length=avg_length
        )

        st.write("🤖 Here's why we chose these movies for you:")
        st.write(explanation)

    else:
        st.error("Sorry, no recommendations found. Please try a different movie.")

with st.expander("See Sample Data"):
    st.dataframe(df.head())
