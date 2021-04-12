
from elasticsearch import Elasticsearch


elastic_client = Elasticsearch(hosts=["http://localhost:9200"])
customerID = 100
fromTime = "2021-04-12T03:48:58+00:00"
toTime = "2021-04-15T04:48:00+00:00"

body = {
    "query": {
        "bool": {
            "must": [{
                "match": {
                    "customer_id": customerID
                    }
            }, {
                "range": {
                    "order_date": {
                        "gte": fromTime,
                        "lte": toTime
                        }
                    }
                }
                ]
            }
        }
    }

res = elastic_client.search(body=body)
print(res['hits']['hits'])
for hit in res['hits']['hits']:
    customer_id = hit["_source"]["customer_id"]
    customer_name = hit["_source"]["customer_full_name"]
    order_id = hit["_source"]["order_id"]
    order_date = hit["_source"]["order_date"]
    product_id = hit["_source"]["products"][1]["product_id"]
    product_name = hit["_source"]["products"][1]["product_name"]
    price = hit["_source"]["products"][1]["price"]

    print("hello",customer_id)


