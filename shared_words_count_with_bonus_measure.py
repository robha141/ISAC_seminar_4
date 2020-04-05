from common import *

# Classes

class QueryItem:
    def __init__(self, word, all_documents):
        self.word = word
        count = 0
        for document in documents:        
            tokenized_document = tokenize(document)
            for word in tokenized_document:
                if self.word in tokenized_document:
                    count += 1
                    break
            
        if count == 0:
            self.bonus = 0
        else:
            self.bonus = 1 / count

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
        if word.word in self.tokenized_document:
            return 1 + word.bonus
        else:
            return 0

    def __str__(self):
        return 'Result: ' + str(self.result) + '\nDocument: ' + self.document + '\n'

# Main

file_name = 'data.txt'
search = 'active learning'

print('🔥 First task 🔥\n')

documents = create_documents_from_file(file_name)
tokenizedSerach = tokenize(search)
query = []
for word in tokenizedSerach:
    query.append(QueryItem(word, documents))
results = []

for document in documents:
    result = Result(document)
    result.calculate_result(query)
    results.append(result)

results.sort(key = lambda result: result.result, reverse = True)
for result in results[:10]:
    print(result)

    