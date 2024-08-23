#!/usr/bin/env python3

'''inserts new document in collection'''


def insert_school(mongo_collection, **kwargs):
    '''returns id'''
    collection = mongo_collection.insert_one(kwargs)
    _id = collection.inserted_id
    return _id
