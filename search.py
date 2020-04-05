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

# First task

def first_task():
    search = "more"
    documents = create_documents_from_file(file_name)
    searchTokens = tokenize(search)
    results = []
    for document in documents:
        documentTokens = tokenize(document)
        hits = 0
        for searchToken in searchTokens:
            if searchToken in documentTokens:
                hits += 1
        result = SharedWorldCountResult(document, hits)
        results.append(result)
    results.sort(key = lambda result: result.resultCount, reverse = True)
    print('🔥 First task 🔥\n')
    for result in results[:10]:
        print('Hits: ' + str(result.resultCount) + '\nDocument: ' + result.document + '\n')
    

def second_task():
    print('Second task')

def third_task():
    print('First task')

def fourth_task():
    print('First task')

if len(sys.argv) > 1:
    taskName = sys.argv[1]

    if taskName == 'firstTask':
        first_task()
    
    if taskName == 'secondTask':
        second_task()

    if taskName == 'thirdTask':
        third_task()

    if taskName == 'fourtTask':
        fourth_task()