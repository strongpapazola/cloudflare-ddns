import requests
import json 

myip = requests.get("http://ifconfig.me").content.decode("UTF-8")
# getiddnsrecord = json.loads(requests.get(
#         url="https://api.cloudflare.com/client/v4/zones/8b43d4a86fc1af806a394d103f0ecd99/dns_records",
#         headers={"Authorization": "Bearer aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Content-Type": "application/json"}
#     ).content.decode("utf-8"))
alldns = json.loads(requests.put(
        url="https://api.cloudflare.com/client/v4/zones/8b43d4a86fc1af806a394d103f0ecd99/dns_records/d8dbb61f26e123344b9af8055ae13046",
        headers={"Authorization": "Bearer aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Content-Type": "application/json"},
        json={"type":"A","name":"example.com","content":myip,"ttl":60,"proxied":True}
    ).content.decode("utf-8"))


print(json.dumps(alldns, indent=3))
