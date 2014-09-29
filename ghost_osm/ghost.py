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
    pass


def authenticate():
    print 'Authenticating to Ghost...'
    if not _is_valid_token():
        print 'Token has expired or is invalid. Regenerating...'
        token = _generate_token()
        config.update_token(token)
        print 'New token generated.'
    print 'Authenticated.'


def _is_valid_token():
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


def _generate_token():
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


def post(osm_posts):
    post_data = _format_post(osm_posts)

    url = 'http://{0}/ghost/api/v0.1/posts'.format(
        config.ghost['base_url']
    )
    data = post_data
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Authorization': 'Bearer {0}'.format(config.ghost['token'])
    }
    print data
    #sys.exit()
    r = requests.post(url, data=data, headers=headers)
    print r.text
    print r.headers
    r.raise_for_status()

    return r.status_code


def _format_post(osm_posts):
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
    post_data = []
    for post in osm_posts:
        post_data.append({
            'status': 'published',
            'title': 'OpenStreetMap Edit - {0}'.format(post['created']),
            'markdown': post['description'],
            'author': 1,
            'created_by': 1,
            'published_by': 1,
            'created_at': post['created'],
            'updated_at': post['created'],
            'published_at': post['created'],
            'tags': ['ghost_osm']
        })
    post_data = {'posts': post_data}

    #return json.dumps(post_data)
    return post_data


if __name__ == '__main__':
    sys.exit(main())
