#!/usr/bin/env python3

'''gives a list of specific topic'''


def schools_by_topic(mongo_collection, topic):
    '''returns a list of specidied topic'''
    return list(mongo_collection.find({"topics": topic}))
