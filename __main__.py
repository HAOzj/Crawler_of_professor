"""
@date: Sep 14th, 2019

@author: woshihaozhaojun@sina.com
"""
from elasticsearch import Elasticsearch
import conf_loader
from bs import main

# by default we connect to localhost:9200
es = Elasticsearch()


def save_es(index, doc_type, profiles):
    for id, profile in enumerate(profiles):
        es.index(index=index,
                 doc_type=doc_type,
                 id=id,
                 body=profile)

    res = es.search(index=index, body={"query": {"match_all": {}}})
    for profile in res["hits"]["hits"]:
        print(profile["_source"]["name"])


if __name__ == "__main__":
    profiles = main()
    save_es(index=conf_loader.index, doc_type=conf_loader.doc_type, profiles=profiles)

