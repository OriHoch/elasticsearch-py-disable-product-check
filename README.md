# Running elasticsearhc-py with disabled product check

In v7.14 of elasticsearch-py a product check was introduced which prevents
using it with an unsupported product.

See [example-success.py](example-success.py) for the code to disable this check.

## Testing the code

### Start an OpenSearch instance

First, we will start an OpenSearch instance to test with. If you have an existing
instance running locally at port 9200 you can skip this step.

```
docker run --name opensearch --rm -d -p 9200:9200 \
    -e "discovery.type=single-node" \
    opensearchproject/opensearch@sha256:405edc708d0f019a3e1224c34029edb9633b79b496bf04e7da4fc3e8b003bcda
```

### Create Python environment

Create the venv

```
python3 -m venv venv
```

Install elasticsearch-py

```
venv/bin/pip install elasticsearch==7.14
```

### Run default client and see it fail

```
venv/bin/python example-error.py
```

Should fail with UnsupportedProductError

### Run modified client and see it succeed

```
venv/bin/python example-success.py
```