#!/usr/bin/python

import os

# this function take an array of strings and 
# returns a dictionary containing each word and a count of times that word is seen
def make_histogram(list):
    histogram = {}
    print "got here"
    print list
    for word in list:
        # TODO: consider trailing punctuation and capitalization
        print word
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    # print histogram
    return histogram


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
    print "-----"
    #do it again
