#!/usr/bin/python3

import sys
import math
import functools
import nltk
from nltk.tokenize import word_tokenize

file_name = 'test.txt'

# Common

class SharedWorldCountResult:
  def __init__(self, document, resultCount):
    self.document = document
    self.resultCount = resultCount

# Splits abstracts in file to array of documents
def create_documents_from_file(file_name):
    documents = []
    with open(file_name) as openfileobject:
        for line in openfileobject:
            documents.append(line)
    return documents

# Returns array of tokens
def tokenize(document):
    return word_tokenize(document)

# Vectors

class Vector:
    # Values are array of int
    def __init__(self, values):
        self.values = values
        
    def dot_product(self, vector):
        if len(vector.values) != len(self.values):
            raise Exception('Vectors do not have same length')
        product = 0
        for index, value in enumerate(self.values):
            product += value * vector.values[index]
        return product
    
    def cosine_similarity(self, vector):
        if len(vector.values) != len(self.values):
            raise Exception('Vectors do not have same length')
        normalized_self = self.normalized()
        normalized_input = vector.normalized()
        dot_product = normalized_self.dot_product(normalized_input)
        return dot_product

    # Returns new normalized vector, not changing current value
    def normalized(self):
        values_pow_two = list(map(lambda x: x**2, values))
        magnitude = math.sqrt(functools.reduce(lambda x, y: x + y, values_pow_two))
        normalized = list(map(lambda x: x * (1 / magnitude), values))
        return Vector(normalized)