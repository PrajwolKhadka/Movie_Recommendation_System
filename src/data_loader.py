# import pandas as pd
# from preprocessing import clean_title
# #Loading the movies dataset
# def load_movies():
#     movie_csv = pd.read_csv('ml-25m/movies.csv')
#     movie_csv["clean_title"] = movie_csv["title"].apply(clean_title)
#     return movie_csv

import pandas as pd
import os
from preprocessing import clean_title

# Loading the movies dataset
def load_movies():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    movie_csv = pd.read_csv(os.path.join(base_dir, '..', 'ml-25m', 'movies.csv'))
    movie_csv["clean_title"] = movie_csv["title"].apply(clean_title)
    return movie_csv

