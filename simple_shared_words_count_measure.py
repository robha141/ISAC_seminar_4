#!/usr/bin/python3

import sys
import csv
import pandas
import numpy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

sw = set(stopwords.words('english'))


# Splits abstracts in file to array of documents
def create_documents_from_file(file_name):
    # read csv file
    data = pandas.read_csv(file_name)
    # get a columns of abstracts
    file = data.abstract
    return file


# Returns array of tokens
def tokenize(document):
    return word_tokenize(document)


def clear_stop_words(document):
    return [word for word in document if not (word.lower() in sw) and len(word) > 1]


class SharedWorldCountResult:
    def __init__(self, document):
        self.document = document
        self.vector = []
        self.res = 0


def print_raw_results(results):
    for swcr in results:
        print(swcr.document, ": ", swcr.vector, ", ", swcr.res)


abstracts = create_documents_from_file('data.csv')

query = "machine learning text"

queryTokens = tokenize(query)

results = []

fileIndex = 0
for file in abstracts:
    file = tokenize(file)
    file = clear_stop_words(file)
    result = SharedWorldCountResult(fileIndex)
    for queryToken in queryTokens:
        if queryToken in file:
            result.vector.append(1)
        else:
            result.vector.append(0)
    result.res = numpy.dot(result.vector, result.vector)
    fileIndex = fileIndex + 1
    results.append(result)

results.sort(key = lambda result: result.res, reverse = True)

print_raw_results(results)
