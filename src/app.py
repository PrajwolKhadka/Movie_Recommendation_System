from data_loader import load_movies
movies = load_movies()
print(movies.head())

from tfidfmatrix import tfidf_class
tfidf_result= tfidf_class()
print(tfidf_result)

# import pandas as pd
# rating_csv = pd.read_csv("ml-25m/ratings.csv")
# print(rating_csv.head())
