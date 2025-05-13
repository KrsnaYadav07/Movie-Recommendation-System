import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

st.title('Movie Recommender System')

selected_movies = st.selectbox(
    'How would you like to be connected?',
    movies['title'].values)

if st.button('Recommend'):
    recommendation = recommend(selected_movies)
    for i in recommendation:
        st.write(i)
