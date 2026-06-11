import streamlit as st
import pandas as pd
import pickle
import difflib

df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.markdown("<h1>Movie Recommendation System🎥</h1",unsafe_allow_html=True)
st.markdown("<h3 style='color:orange;'>Get movie recommendations based on content similarity.</h3>",unsafe_allow_html=True)
st.write("Discover movies similar to your favorites [ ▸ ]")

movie_name = st.text_input("Enter Movie Name")

if st.button("Recommend"):

    list_of_all_titles = df['title'].tolist()

    find_close_match = difflib.get_close_matches(
        movie_name,
        list_of_all_titles
    )

    if len(find_close_match)==0:
        st.error("Movie not found in the dataset")
    else:

        close_match = find_close_match[0]

        index_of_the_movie = df[
            df['title'] == close_match
        ]['index'].values[0]

        similarity_score = list(
            enumerate(similarity[index_of_the_movie])
        )

        sorted_similar_movies = sorted(
            similarity_score,
            key=lambda x: x[1],
            reverse=True
        )

        st.success(f"Showing recommendations for: {close_match}")

        i = 1

        for movie in sorted_similar_movies:

            index = movie[0]

            title_from_index = df[
                df['index'] == index
            ]['title'].values[0]

            if i < 10:
                st.write(f"{i}. {title_from_index}")
                i += 1