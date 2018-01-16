#!/usr/bin/python

import os
from string import punctuation

# create collection of histograms
counts = {}

def main():
    # open each file
    for filename in os.listdir("./sona"):
        path = "./sona/" + filename
        file = open(path, "r")
        h = make_histogram(file)
        # save this in "counts" as filename -> histogram
        counts[filename] = h

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
            # add to histogram
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
    return histogram
    
main()
print counts

# each document will need a histogram
# the entire corpus will need a histogram

# then I should look at the top 'x' tf-idf scores of each document
