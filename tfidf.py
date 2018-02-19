#!/usr/bin/python

import os
from string import punctuation
import operator
import math

# create collection of histograms
# blacklist = {"the", "not", "and", "or", "like", "of", "to", "in", "we", "a", "that", "our", "will", "for", "is", "this", "have", "as", "all", "are", "be", "with", "on", "by", "also", " ", "should", "which", "has", "at", "it", "their", "us", "year", "these", "from", "they"}

# key is filename
# value is histogram
counts = {}
tfs = {}
tfidfs = {}
numberOfDocs = 0

def main():
    count_dir("small_set")

def count_dir(path):
    global counts
    global tfs
    global tfidfs
    global numberOfDocs
    # open each file
    files = os.listdir("./samples/" + path)
    numberOfDocs = len(files) # TODO, shouldn't recalculate this so many times

    for filename in files:
        file = open("./samples/" + path + "/" + filename, "r")
        # save this in "counts" as filename -> histogram        
        counts[filename] = make_histogram(file)
        # save this in "tfs" as filename -> term freqs
    for filename in files:
        tfs[filename] = makeTF(counts[filename])
        # calculate tfidfs, given the term freqs.
    for filename in files:
        tfidfs[filename] = makeTFIDF(tfs[filename])

def makeTF(hist):
    tf = {}
    # print "makeTF for hist: ", hist
    # we have the number of times for a term
    # we need to divide it by the number of words in the document
    termCount = 0.0
    for word in hist:
        termCount += hist[word]
    
    # print "TERM COUNT: ", termCount

    for word in hist:
        tf[word] = hist[word]/termCount
        # print "word: ", word
        # print "tf[word]: ", tf[word]
    
    return tf

# function to strip punctuation from a string
# i.e. "almost," -> "almost"
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

# function takes a file and 
# returns a dictionary containing each word and a count of times that word is seen
def make_histogram(file):
    histogram = {}
    for line in file:
        for word in line.split():
        	# lowercase'd and getting rid of trailing punctuation
            word = strip_punctuation(word).lower()
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
    return histogram

def makeTFIDF(tfs):
    tfidf = {}
    for word in tfs:
        # print "Considering word: ", word
        numberOfDocsWithTerm = 0.0;
        # TF
        tf = tfs[word]
        # IDF = log_e (total number of docs / number of docs with term in it)
        # num of Docs with term in it
        for doc in counts:
            if word in counts[doc]:
                numberOfDocsWithTerm += 1
        wordTFIDF = math.log(numberOfDocs/numberOfDocsWithTerm)
        tfidf[word] = wordTFIDF
        print "word:", word, " - numberOfDocs:", numberOfDocs, " - numberOfDocsWithTerm:", numberOfDocsWithTerm, "TFIDF:",wordTFIDF
    return tfidf

def most(doc):
    global tfidfs
    print "most relevant terms in ", doc
    dict = tfidfs[doc]
    print dict
    words_ordered_descending_length = sorted(dict, key=dict.get, reverse=True)
    print words_ordered_descending_length

if __name__ == '__main__':
    main()
    first = next(iter(tfs))
    print "--- COUNTS ---"
    print counts[first]
    print "--- TERM FREQS ---"
    print tfs[first]
    print "--- TF-IDFS ---"
    print tfidfs[first]
    print "--- MOST RELEVANT TERMS ---"
    print most(first)

# Calculate term frequency
# TF(t) = (Number of times term t appears in a document) 
#            / (Total number of terms in the document).

# Calculate idf
# IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

