import pandas as pd
#Loading the movies dataset
movie_csv= pd.read_csv('ml-25m/movies.csv')
print(movie_csv.head())

import re
#Cleaning movie titles
def clean_title(title):
    return re.sub("[a-zA-Z0-9]","",title)
     