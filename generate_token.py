#!/usr/bin/python

import requests
import json
import pprint
import yaml

with open('auth.yml', 'r') as config_fh:
    auth = yaml.load(config_fh)

url = '{base_url}/ghost/api/v0.1/authentication/token'.format(
    base_url = 'http://blog.cptmorgan.com'
)
post_data = 'grant_type=password&username={username}&password={password}&client_id=ghost-admin'.format(
    username = auth['username'],
    password = auth['password']
)
headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
}

r = requests.post(url, data=post_data, headers=headers)
r.raise_for_status()
pprint.pprint(json.loads(r.text))