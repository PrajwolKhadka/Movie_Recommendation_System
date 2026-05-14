from sklearn.feature_extraction.text import TfidfVectorizer
from data_loader import load_movies

def tfidf_class():
    movie_csv=load_movies()
    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    tfidf = vectorizer.fit_transform(movie_csv["clean_title"])
    return vectorizer,tfidf

# POTTER THE HARRY
# 0       1    0
# 0       1    1
# 1       1    1

# POTTER      THE         HARRY
# log(3/1)     log(3/3)    log(3/2)
# log(3/1)     log(3/3)   log(3/2)
# log(3/1)     log(3/3)   log(3/2)

# TF*IDF

# POTTER   THE      HARRY
# 0          0          0      0.0
# 0.477    00       0 .176      1.0
# 0       0         0.176       0.176

# Harry Potter

# THE 
# THE HARRY 
# THE HARRY POTTER 
