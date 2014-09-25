import sys
import config
import requests
import json


def main():
    print generate_token()


def generate_token():
    url = 'http://{0}/ghost/api/v0.1/authentication/token'.format(
        config.ghost['base_url']
    )
    data = 'grant_type=password&username={0}&password={1}&client_id=ghost-admin'.format(
        config.ghost['username'],
        config.ghost['password']
    )
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
    }

    r = requests.post(url, data=data, headers=headers)
    r.raise_for_status()
    return json.loads(r.text)['access_token']


if __name__ == '__main__':
    sys.exit(main())
