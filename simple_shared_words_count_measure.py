from common import *

# Classes

class Result:
    def __init__(self, document):
        self.document = document
        self.tokenized_document = tokenize(document)
        self.vector = []

    def calculateVector(self, query):
        for word in query:
            w = self.calculateW(word)
            self.vector.append(w)

    def calculateW(self, word):
        if word in self.tokenized_document:
            return 1
        else:
            return 0

# Main

file_name = 'test.txt'
search = 'more data'

print('🔥 First task 🔥\n')

documents = create_documents_from_file(file_name)
query = tokenize(search)
results = []

for document in documents:
    result = Result(document)
    result.calculateVector(query)
    results.append(result)

for result in results:
    print(result.vector)