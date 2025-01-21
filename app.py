import streamlit as st
import pandas as pd
import pickle 
import os


movie_dict=pickle.load(open(r"C:\Users\Anjana\OneDrive\Desktop\sample\artifacts\movies_dict.pkl",'rb'))
movies=pd.DataFrame(movie_dict)


# Load the files
try:
    with open(r"C:\Users\Anjana\OneDrive\Desktop\sample\artifacts\movie_list.pkl", 'rb') as movie_file:
        movie_list = pickle.load(movie_file)

    with open(r"C:\Users\Anjana\OneDrive\Desktop\sample\artifacts\similiarity.pkl", 'rb') as similarity_file:
        similarity = pickle.load(similarity_file)
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()

def recommend(movie):
    movi_index=movies[movies['title']==movie].index[0]
    distance=similarity[movi_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]
    for i in movies_list:
        movie_id=i[0]
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

# Streamlit app
st.title("Movie Recommendation System")

# Dropdown for movie selection
selected_movie_name=st.selectbox(
    "Enter movie : ",movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

