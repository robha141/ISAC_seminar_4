from common import *

# Classes

class Result:
    def __init__(self, document):
        self.document = document
        self.tokenized_document = tokenize(document)
        self.vector = []
        self.result = 0

    def calculate_result(self, query):
        for word in query:
            w = self.calculate_w(word)
            self.vector.append(w)
        self.calculate_cross_product(query)

    def calculate_cross_product(self, query):
        result = 0
        for value in self.vector:
            result = result + (value * 1)
        self.result = result

    def calculate_w(self, word):
        if word in self.tokenized_document:
            return 1
        else:
            return 0

    def __str__(self):
        return 'Result: ' + str(self.result) + '\nDocument: ' + self.document

# Main

file_name = 'data.txt'
search = 'active learning'

print('🔥 First task 🔥\n')

documents = create_documents_from_file(file_name)
query = tokenize(search)
results = []

for document in documents:
    result = Result(document)
    result.calculate_result(query)
    results.append(result)

results.sort(key = lambda result: result.result, reverse = True)
for result in results[:10]:
    print(result)