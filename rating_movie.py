import pandas as pd
#Loading the ratings dataset
def load_ratings():
    ratings_csv = pd.read_csv('ml-25m/ratings.csv')
    return ratings_csv
print(load_ratings().head())