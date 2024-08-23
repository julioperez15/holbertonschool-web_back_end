#!/usr/bin/env python3

'''changes all topics of a document'''


def update_topics(mongo_collection, name, topics):
    '''returns update dictionary'''
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
