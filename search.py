#!/usr/bin/python3

import sys

file_name = 'test.txt'

def create_documents_from_file(file_name):
    documents = []
    with open(file_name) as openfileobject:
        for line in openfileobject:
            documents.append(line)
    return documents

def first_task():
    print('First task')

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