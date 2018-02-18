#!/usr/bin/python

import os
from string import punctuation
import operator

# create collection of histograms
# blacklist = {"the", "not", "and", "or", "like", "of", "to", "in", "we", "a", "that", "our", "will", "for", "is", "this", "have", "as", "all", "are", "be", "with", "on", "by", "also", " ", "should", "which", "has", "at", "it", "their", "us", "year", "these", "from", "they"}

# key is filename
# value is histogram
counts = {}
tfs = {}

def main():
    count_dir("sona")

def count_dir(path):
    global counts
    global tfs
    # open each file
    for filename in os.listdir("./samples/" + path):
        file = open("./samples/" + path + "/" + filename, "r")
        # save this in "counts" as filename -> histogram        
        counts[filename] = make_histogram(file)
        # save this in "tfs" as filename -> term freqs
        tfs[filename] = makeTF(counts[filename])

#    print "*****"
#    print counts
#    print len(counts)
#    print "*****"

def makeTF(hist):
    tf = {}
    # we have the number of times for a term
    # we need to divide it by the number of words in the document
    termCount = 0.0
    for word in hist:
        termCount += hist[word]
    
    print "TERM COUNT: ", termCount

    for word in hist:
        tf[word] = hist[word]/termCount
    
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
            #if word in blacklist:
            #    continue    
            # add to histogram
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
    return histogram

# each document will need a histogram
# the entire corpus will need a histogram

# then I should look at the top 'x' tf-idf scores of each document

# Just print the most common words in each speech.
#for document in counts:
#    print document
#    print max(counts[document].iteritems(), key=operator.itemgetter(1))[0]

if __name__ == '__main__':
    main()
    # print "--- COUNTS ---"
    # print counts[next(iter(counts))]

    print "--- TERM FREQS ---"
    print tfs[next(iter(tfs))]


# Calculate term frequency
# TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).

# Calculate idf
# IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

