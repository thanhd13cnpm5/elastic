from elasticsearch import Elasticsearch

elastic_client = Elasticsearch(hosts=["http://localhost:9200"])

print("-Search by order_date")
start = input("-from time: ")
end = input("-to time: ")
body = {
  "query": {
    "range": {
      "order_date": {
        "gte": start,
        "lte": end
      }
    }
  }
}

res = elastic_client.search(body=body)
for hit in res['hits']['hits']:
    print("id: ", hit["_id"]+" / index: ", hit["_index"]+" / category: ", hit["_source"]["category"]," /customerID: "
    ,hit["_source"]["customer_id"]," / customer_full_name: ", hit["_source"]["customer_full_name"] + " / order_id: ",
    hit["_source"]["order_id"], " / order_date: ", hit["_source"]["order_date"])

#2021-04-12T03:48:58+00:00
#2021-04-15T04:48:00+00:00

#kết quả
# id:  ksaMsHgBRitmfRxkeQQo / index:  kibana_sample_data_ecommerce / category:  ["Women's Accessories", "Women's Clothing", "Women's Shoes"]  /customerID:  5  / customer_full_name:  Rabbia Al Romero / order_id:  727381  / order_date:  2021-04-12T10:46:34+00:00
# id:  lcaMsHgBRitmfRxkeQQo / index:  kibana_sample_data_ecommerce / category:  ["Men's Clothing"]  /customerID:  38  / customer_full_name:  Eddie Wolfe / order_id:  715061  / order_date:  2021-04-12T19:59:31+00:00
# id:  lsaMsHgBRitmfRxkeQQo / index:  kibana_sample_data_ecommerce / category:  ["Men's Clothing", "Men's Shoes", "Women's Accessories"]  /customerID:  19  / customer_full_name:  Sultan Al Thompson / order_id:  721826  / order_date:  2021-04-13T21:24:29+00:00
# id:  mMaMsHgBRitmfRxkeQQo / index:  kibana_sample_data_ecommerce / category:  ["Men's Clothing", "Men's Shoes"]  /customerID:  32  / customer_full_name:  George Hubbard / order_id:  578916  / order_date:  2021-04-15T04:48:00+00:00
# id:  mcaMsHgBRitmfRxkeQQo / index:  kibana_sample_data_ecommerce / category:  ["Men's Clothing"]  /customerID:  36  / customer_full_name:  Boris Maldonado / order_id:  578355  / order_date:  2021-04-14T18:23:02+00:00
# id:  msaMsHgBRitmfRxkeQQo / index:  kibana_sample_data_ecommerce / category:  ["Men's Clothing"]  /customerID:  23  / customer_full_name:  Yahya Rivera / order_id:  576663  / order_date:  2021-04-13T11:32:38+00:00
# id:  m8aMsHgBRitmfRxkeQQo / index:  kibana_sample_data_ecommerce / category:  ["Women's Clothing", "Women's Accessories"]  /customerID:  12  / customer_full_name:  Brigitte Morris / order_id:  576696  / order_date:  2021-04-13T12:15:50+00:00
# id:  nMaMsHgBRitmfRxkeQQo / index:  kibana_sample_data_ecommerce / category:  ["Women's Accessories", "Women's Shoes"]  /customerID:  42  / customer_full_name:  Selena Bryant / order_id:  575420  / order_date:  2021-04-12T12:47:31+00:00
# id:  osaMsHgBRitmfRxkeQQo / index:  kibana_sample_data_ecommerce / category:  ["Women's Clothing"]  /customerID:  28  / customer_full_name:  Sonya Foster / order_id:  576925  / order_date:  2021-04-13T16:07:41+00:00
