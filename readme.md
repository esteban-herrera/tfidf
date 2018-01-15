# tf-idf practice

This project will implement a tf-idf algorithm and return the highest tf-idf-scored words for each file in the corpus.

The data set was acquired from kaggle.com here https://www.kaggle.com/allank/state-of-the-nation-1990-2017/data

It is a collection of the text of the State of the Nation Address of the South African president since 1990.

---

As a reference, I'm using the definition of tf-idf found here, and will link all other resources I end up using:

http://www.tfidf.com/

"""
TF: Term Frequency, which measures how frequently a term occurs in a document. Since every document is different in length, it is possible that a term would appear much more times in long documents than shorter ones. Thus, the term frequency is often divided by the document length (aka. the total number of terms in the document) as a way of normalization: 

TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).

IDF: Inverse Document Frequency, which measures how important a term is. While computing TF, all terms are considered equally important. However it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. Thus we need to weigh down the frequent terms while scale up the rare ones, by computing the following: 

IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
"""