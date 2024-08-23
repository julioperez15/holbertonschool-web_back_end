#!/usr/bin/env python3

'''This function lists all documents'''


def list_all(mongo_collection):
    '''returns a list'''
    return mongo_collection.find()
