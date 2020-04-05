from common import *

file_name = 'test.txt'

class QueryToken:
    def __init__(self, token):
        self.token = token
        self.hits = 0

class Vector:
    def __init__(self, query):
        self.queryTokens = map(lambda token: QueryToken(token), query)

    def add_hit(self, token):
        for queryToken in self.queryTokens:
            if queryToken.token == token:
                queryToken.hits += 1

    # Returns vector as array of int
    def get_vector_value(self):
        return map(lambda queryToken: queryToken.hits, self.queryTokens)

class DocumentVectorizer:
    def __init__(self, document):
        self.document = document

    def generate_vector(self, query):
        document_tokens = tokenize(self.document)
        vector = Vector(query)
        for token in document_tokens:
            vector.add_hit(token)
        return vector.get_vector_value


search = "more"
query = "more"

print('🔥 First task 🔥\n')

documents = create_documents_from_file(file_name)
query = tokenize(search)
for document in documents:
    vectorizer = DocumentVectorizer(document)
    vector = vectorizer.generate_vector(query)
    print(vector)


