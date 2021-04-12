from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route("/getInfo", methods=["GET", "POST"])
def getInfo():
    try:#check for connect to elastic
        elastic_client = Elasticsearch(hosts=["http://localhost:9200"])

        if type(request.json["customerID"]) is int and request.json["customerID"] > 0:#check customerID
            customerID = request.json["customerID"]# lấy customerID
        else:
            return jsonify("error : maybe customerID is str or customerID < 0. Please check again!")
        fromTime = request.json["fromTime"]#lấy khoảng thời gian tìm kiếm
        toTime = request.json["toTime"]
        List_Order = []

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

        if not res['hits']['hits']:#check customer_id exist or not
            return jsonify("no have this customerID!")
        else:
            for hit in res['hits']['hits']:
                customer_id = hit["_source"]["customer_id"]
                customer_name = hit["_source"]["customer_full_name"]
                order_id = hit["_source"]["order_id"]
                order_date = hit["_source"]["order_date"]
                product_id = hit["_source"]["products"][1]["product_id"]
                product_name = hit["_source"]["products"][1]["product_name"]
                price = hit["_source"]["products"][1]["price"]

                order = {
                    "customer_id": customer_id,
                    "customer_name": customer_name,
                    "order_id": order_id,
                    "order_date": order_date,
                    "product_id": product_id,
                    "product_name": product_name,
                    "price": price
                }

                List_Order.append(order)

            if not List_Order:#check list nếu rỗng
                return jsonify("no product ordered!")
            return jsonify(List_Order)#trả ra list order
    except:
        #connect failure
        return jsonify("Connect to elastic is failure!")

if __name__=="__main__":
    app.run(debug=True)



#input
# {
#     "customerID": 39,
#     "fromTime": "2021-04-12T03:48:58+00:00",
#     "toTime": "2021-04-15T04:48:00+00:00"
# }

#output
# [
#     {
#         "customer_id": 39,
#         "customer_name": "Kamal Hale",
#         "order_date": "2021-04-13T00:59:02+00:00",
#         "order_id": 576071,
#         "price": 49.99,
#         "product_id": 13275,
#         "product_name": "Rucksack - grey"
#     },
#     {
#         "customer_id": 39,
#         "customer_name": "Kamal Estrada",
#         "order_date": "2021-04-12T23:47:02+00:00",
#         "order_id": 575988,
#         "price": 41.99,
#         "product_id": 7092,
#         "product_name": "Tracksuit top - oliv"
#     },
#     {
#         "customer_id": 39,
#         "customer_name": "Kamal Cortez",
#         "order_date": "2021-04-13T02:41:17+00:00",
#         "order_id": 576171,
#         "price": 24.99,
#         "product_id": 19297,
#         "product_name": "Trainers - white"
#     },
#     {
#         "customer_id": 39,
#         "customer_name": "Kamal Salazar",
#         "order_date": "2021-04-13T17:12:29+00:00",
#         "order_id": 576983,
#         "price": 64.99,
#         "product_id": 23027,
#         "product_name": "Boots - Midnight Blue"
#     },
#     {
#         "customer_id": 39,
#         "customer_name": "Kamal Conner",
#         "order_date": "2021-04-12T11:02:24+00:00",
#         "order_id": 575316,
#         "price": 20.99,
#         "product_id": 17428,
#         "product_name": "Sweatshirt - bordeaux"
#     },
#     {
#         "customer_id": 39,
#         "customer_name": "Kamal Brock",
#         "order_date": "2021-04-14T16:53:46+00:00",
#         "order_id": 578286,
#         "price": 84.99,
#         "product_id": 1844,
#         "product_name": "Boots - beige"
#     }
# ]