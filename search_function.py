from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from data_loader import load_movies
movie_csv = load_movies()
from tfidfmatrix import tfidf_class
vectorizer, tfidf = tfidf_class()

def search(title):
    query_vector = vectorizer.transform([title])
    cosine_similarities = cosine_similarity(query_vector, tfidf).flatten()
    top_indices = np.argpartition(cosine_similarities, -5)[-5:]
    return movie_csv.iloc[top_indices][::-1]

# print(search("Toy Story 1995"))