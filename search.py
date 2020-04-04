file_name = 'test.txt'

def create_documents_from_file(file_name):
    documents = []
    with open(file_name) as openfileobject:
        for line in openfileobject:
            documents.append(line)
    return documents


documents = create_documents_from_file(file_name)
print(documents)





