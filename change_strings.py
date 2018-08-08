import requests
import json

url = "http://localhost:8080/api/config/snmp-strings/foo"

payload = {"snmp-strings:snmp-strings": {
             "name": "foo",
             "readonly": "notsecure",
             "readwrite": "stillnotsecure"
             }
          }
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46YWRtaW4=",
    'Accept': "application/vnd.yang.collection+json, application/vnd.yang.data+json,pplication/vnd.yang.datastore+json, application/vnd.yang.datastore+json"
    }

response = requests.request("PATCH", url, data=json.dumps(payload), headers=headers)

print(response.text)
