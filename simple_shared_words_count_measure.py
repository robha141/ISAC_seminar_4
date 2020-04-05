from common import *

file_name = 'test.txt'

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
    if hits > 0:
        result = SharedWorldCountResult(document, hits)
        results.append(result)
results.sort(key = lambda result: result.resultCount, reverse = True)
print('🔥 First task 🔥\n')
for result in results[:10]:
    print('Hits: ' + str(result.resultCount) + '\nDocument: ' + result.document + '\n')