import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ---- Load preprocessed data ----
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("🎬 Movie Recommender System")
st.markdown("Type or choose a movie to get similar movie suggestions.")

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

def recommend(movie_title):
    """Return a list of 5 recommended movie titles."""
    index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[index]
    movie_indices = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    return [movies.iloc[i[0]].title for i in movie_indices]

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("You might also like:")
    for i, rec in enumerate(recommendations, start=1):
        st.write(f"{i}. {rec}")
