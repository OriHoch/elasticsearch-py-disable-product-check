import elasticsearch


es = elasticsearch.Elasticsearch(['https://admin:admin@localhost:9200'], verify_certs=False)
print(es.info())