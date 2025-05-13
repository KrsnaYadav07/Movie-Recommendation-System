# Movie-Recommendation-System
This is a simple Movie Recommender System built using Streamlit and Python. The system recommends movies based on a user's selected movie using a pre-trained similarity matrix.

Features
Movie Recommendation: Select a movie, and the system will recommend 5 similar movies based on content similarity.

Interactive UI: Built with Streamlit, the app provides an intuitive user interface where users can interact and get recommendations in real-time.

The datasets used in this project are:
1. `tmdb_5000_movies.csv`: Contains information about movies such as budget, genres, title, revenue, etc.
2. `tmdb_5000_credits.csv`: Contains information about movie credits such as the cast and crew of the movies.

## Project Description

This project involves:
- Merging data from two CSV files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) into a single dataframe.
- Cleaning and transforming the data by:
  - Parsing and converting nested JSON structures within columns like `genres`, `keywords`, `cast`, and `crew`.
  - Extracting and processing relevant information such as genres, keywords, top 3 cast members, and the director.
  - Creating a new `tag` column by combining the `overview`, `genres`, `keywords`, `cast`, and `crew`.

The final output is a dataset ready for analysis, machine learning, or content-based recommendation systems.
