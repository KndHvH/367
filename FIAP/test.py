
import requests

import json

url = 'http://0.0.0.0:8000/v1/sentiment'

response = requests.get(url)

comment = {
  "text": "Customer dissatisfied with product delivery deadlines, worried and limited products/volumes for new negotiation., alternative is to migrate to competitors and open doors to new experiences. I shared with him our problems with cost increases and product supply, caused by problems generated due to global market and political movement, as we depend on active ingredients supplied by other countries. The grade 5 in delivery reliability was generated due to delays in deliveries compared to the initial schedule passed by the customer.",
  "note": 6,
  "companyId": 1940324,
  "responseDate": "2022-09-29T23:10:54.640Z"
}

response = requests.post(url,data=json.dumps(comment))



print(response.json())

# link = "https://ousadia-api.herokuapp.com/v1/sentiment"

# print(link.get)