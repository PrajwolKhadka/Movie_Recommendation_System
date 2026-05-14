from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from data_loader import load_movies
movie_csv = load_movies()

from tfidfmatrix import tfidf_class
vectorizer, tfidf = tfidf_class(movie_csv)

def search(title):
    query_vector = vectorizer.transform([title])
    cosine_similarities = cosine_similarity(query_vector, tfidf).flatten()
    top_indices = np.argpartition(cosine_similarities, -5)[-5:]
    top_indices = top_indices[np.argsort(cosine_similarities[top_indices])[::-1]]
    return movie_csv.iloc[top_indices][["movieId", "title", "clean_title", "genres"]]

# print(search("Toy Story 1995"))