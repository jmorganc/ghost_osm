"""
@TODO
    -

Endpoints: https://github.com/TryGhost/Ghost/wiki/%5BWIP%5D-API-Documentation#endpoints
    /ghost/api/v0.1/posts/1/
"""

import sys
import config
import requests
import json
import time


def main():
    token = config.ghost['token']
    if not is_valid_token():
        token = generate_token()
        config.update_token(token)


def is_valid_token():
    if time.time() - config.ghost['token_timestamp'] >= config.ghost['token_expiry']:
        print 'Token expired'
        return False
    return True
    # headers = {
    #     'Authorization': 'Bearer {0}'.format(token)
    # }
    # r = requests.get('http://{0}/ghost/api/v0.1/users/me/'.format(config.ghost['base_url']), headers=headers)
    #
    # if r.status_code != 200:
    #     if r.status_code == 401:
    #         print '401: Unauthorized, need to get a token'
    #         return False
    #     else:
    #         r.raise_for_status()
    # else:
    #     print '200: It works'
    #     return True


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
