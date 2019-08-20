import requests
from requests.auth import HTTPBasicAuth


r = requests.get('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', '1a2b3c4d'), verify=False)

print("status: {}".format(r.status_code))

print("text: {}".format(r.text))

