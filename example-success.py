import elasticsearch


class TransportWithoutVerify(elasticsearch.transport.Transport):

    def __init__(self, *args, **kwargs):
        super(TransportWithoutVerify, self).__init__(*args, **kwargs)
        self._verified_elasticsearch = True


es = elasticsearch.Elasticsearch(['https://admin:admin@localhost:9200'], verify_certs=False, transport_class=TransportWithoutVerify)
print(es.info())