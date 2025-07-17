import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url).json()

    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return "https://via.placeholder.com/500"  # Placeholder image if no poster found


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]  # Get index of selected movie
        distances = similarity[movie_index]  # Get similarity scores
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # Top 5 recommendations

        recommended_movies = []
        recommended_movies_posters = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id  # Fix incorrect variable
            recommended_movies.append(movies.iloc[i[0]].title)  # Append movie title
            recommended_movies_posters.append(fetch_poster(movie_id))  # Fetch poster

        return recommended_movies, recommended_movies_posters  # Return both lists

    except IndexError:
        return [], []  # Return empty lists if no recommendations found


# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox("Select a movie:", movies['title'].tolist())

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    if recommended_movie_names:  # Check if recommendations exist
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
    else:
        st.warning("No recommendations found. Please try another movie.")
