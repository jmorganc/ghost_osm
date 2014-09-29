"""
@TODO
    -

Endpoints: https://github.com/TryGhost/Ghost/wiki/%5BWIP%5D-API-Documentation#endpoints
    /ghost/api/v0.1/posts/1/
"""

import sys
import requests
import json
import time

import config


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


def post():
    """
    {
        posts: [
            {
                status: "published",
                id: 1,
                uuid: "ec630e45-3342-4d7f-a24c-e448263c975b",
                title: "Welcome to Ghost",
                slug: "welcome-to-ghost",
                markdown: "",
                html: "",
                image: null,
                featured: false,
                page: false,
                language: "en_US",
                meta_title: null,
                meta_description: null,
                author: 1,
                created_at: "2014-04-15T12:36:28.353Z",
                created_by: 1,
                updated_at: "2014-04-15T12:36:28.353Z",
                updated_by: 1,
                published_at: "2014-04-15T12:36:28.363Z",
                published_by: 1,
                tags: [{ ... }]
            }
        ]
    }
    """
    pass


if __name__ == '__main__':
    sys.exit(main())
