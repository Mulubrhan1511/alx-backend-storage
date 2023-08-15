#!/usr/bin/env python3
""" MongoDB Operations with Python using """

def list_all(collection):
    # Retrieve all documents from the collection
    documents = collection.find()

    # Check if the cursor is empty
    if documents.count_documents({}) == 0:
        print("No documents found.")
        return []

    # Return the list of documents
    return list(documents)
