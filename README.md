# 🎬 Movie Recommender System

This is a simple yet powerful **Movie Recommender System** built using **Python** and **Streamlit**. It recommends similar movies based on the selected movie using a pre-computed similarity matrix and content-based filtering techniques.

---

## ✨ Features

- 🔍 **Content-Based Movie Recommendation**  
  Select a movie and get 5 similar movie suggestions based on plot, cast, genre, keywords, and director.

- ⚡ **Real-time Interactive UI**  
  Built with **Streamlit**, the app offers an intuitive interface for quick and easy recommendations.

- 🧠 **NLP-powered Similarity Engine**  
  Uses **TF-IDF** vectorization and **cosine similarity** on processed tags to generate recommendations.

---

## 📁 Datasets Used

The system uses data from **The Movie Database (TMDB)**:

- `tmdb_5000_movies.csv`: Contains metadata like budget, genres, title, revenue, etc.
- `tmdb_5000_credits.csv`: Contains information about cast and crew.

Available on [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

---

## 🛠️ How It Works

1. **Merge & Clean Data**
   - Combined `movies` and `credits` datasets using movie IDs.
   - Parsed nested JSON fields like `genres`, `keywords`, `cast`, and `crew`.

2. **Extract & Engineer Features**
   - Extracted top 3 cast members and director.
   - Combined overview, genres, keywords, cast, and crew into a single `tags` column.

3. **Vectorization & Similarity**
   - Used **TF-IDF** to convert tags into numerical vectors.
   - Calculated **cosine similarity** to find and rank similar movies.

4. **Streamlit UI**
   - Deployed a simple interface where users can select a movie and view 5 recommendations instantly.

---
##🧠 Tech Stack
1.Python
2.Pandas
3.Scikit-learn
4.Streamlit
5.TF-IDF
