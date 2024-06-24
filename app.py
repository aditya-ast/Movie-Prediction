import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index] 
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:11]
    
    recommend_movie = []
    for i in movie_list:
        movie_id = i[0]
        # fetch poster from api
        
        
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie
        
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
        
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = pickle.load(open('movie.pkl', 'rb'))
movie_list = movie_list['title'].values

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie do you like best?',
    movie_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    
    for i in recommendations:
        st.write(i)