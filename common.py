#!/usr/bin/python3

import sys
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