# import pandas as pd
# # #Loading the ratings dataset
# def load_ratings():
#     ratings_csv = pd.read_csv('ml-25m/ratings.csv')
#     return ratings_csv
# # print(load_ratings().head(n=10))
# # ratings_csv = pd.read_csv('ml-25m/ratings.csv')
# # print(ratings_csv.dtypes)

import pandas as pd
import os

def load_ratings():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ratings_csv = pd.read_csv(os.path.join(base_dir, '..', 'ml-25m', 'ratings.csv'))
    return ratings_csv