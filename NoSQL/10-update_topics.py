#!/usr/bin/env python3
"""Module for updating topics in a MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """Change all topics of a school document based on the name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
        )
