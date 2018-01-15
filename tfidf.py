#!/usr/bin/python

import os
from string import punctuation


# function to strip punctuation from a sting
# i.e. "almost," -> "almost"
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

# this function take an array of strings and 
# returns a dictionary containing each word and a count of times that word is seen
def make_histogram(list):
    histogram = {}
    print "got here"
    print list
    for word in list:
        # get rid of punctuation and make them all lowercase
        word = strip_punctuation(word)
        word = word.lower()

        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    # print histogram
    return histogram



# create collection of histograms
counts = {}

# open each file
for filename in os.listdir("./sona"):
    # print(filename)
    path = "./sona/" + filename
    file = open(path, "r")
    # file is open, now split and read into an array
    data = file.read().split()
    # count instances of each word
    h = make_histogram(data)
    print h
    counts[filename] = h
    print "-----"
    #do it again

print counts


# each document will need a histogram
# the entire corpus will need a histogram

# then I should look at the top 'x' tf-idf scores of each document
