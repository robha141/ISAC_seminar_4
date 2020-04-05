from common import *

# Helping classes

class Result:
    def __init__(self, document, cosine_similiarity):
        self.document = document
        self.cosine_similiarity = cosine_similiarity

    def __str__(self):
        return 'Cosine similiarity: ' + str(self.cosine_similiarity) + '\nDocument: ' + self.document + '\n'

# Main

print('🔥 Cosine similarity measure using only the term frequency weight 🔥\n')

file_name = 'data.txt'
search = 'active data'
try:
    search = sys.argv[1]
    print('Using query: \'' + search + '\'')
except IndexError:
    print('No query provided, using \'active learning\'')  

try:
    file_name = sys.argv[2]
    print('Using file: \'' + file_name + '\'')
except IndexError:
    print('No file name provided, using \'data.txt\'')  

# lebo tam ma napadá:
# získame si query vector
# 	z každého dokumentu si spravíme vektor a normalizujme ho (keď robím term frequency, inak ešte musím vynásobiť tou konštantou na inverse document frequency)
# 	spravíme cosine simularity týchto dvoch vectorov
# 	uložím a zoradím

documents = create_documents_from_file(file_name)
query = tokenize(search)
query_vector = Vector(list(map(lambda x: 1, query)))
results = []

for document in documents:
    term_frequency = list(map(lambda x: 0, query))
    tokenizedDocument = tokenize(document)
    for word in tokenizedDocument:
        if word in query:
            index_of_word = query.index(word)
            term_frequency[index_of_word] += 1
    document_vector = Vector(term_frequency)
    cosine_similiarity = document_vector.cosine_similarity(query_vector)
    result = Result(document, cosine_similiarity)
    results.append(result)

results.sort(key = lambda result: result.cosine_similiarity, reverse = True)
for result in results[:10]:
    print(result)


