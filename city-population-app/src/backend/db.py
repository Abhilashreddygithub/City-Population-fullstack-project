from elasticsearch import Elasticsearch

def get_es():
from elasticsearch import Elasticsearch
import os

def get_es():
    """Return an Elasticsearch client using ELASTICSEARCH_URL env var.

    Defaults to http://localhost:9200 which is convenient when running ES in Docker.
    """
    url = os.environ.get("ELASTICSEARCH_URL", "http://localhost:9200")
    return Elasticsearch(url)