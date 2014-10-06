import yaml
import time


with open('auth.yml', 'r') as auth_fh:
    auth = yaml.load(auth_fh)

ghost = {
    'base_url': 'blog.cptmorgan.com',
    'username': auth['username'],
    'password': auth['password'],
    'token': auth['token'],
    'token_refresh': auth['token_refresh'],
    'token_timestamp': auth['token_timestamp'],
    'token_expiry': 3600,
    'token_refresh_expiry': 86400
}

osm = {
    'username': 'Obrit'
}


def update_token(token_new, token_refresh):
    with open('auth.yml', 'w') as auth_fh:
        auth_fh.write('---\nusername: {0}\npassword: {1}\ntoken: {2}\ntoken_refresh: {3}\ntoken_timestamp: {4}\n'.format(
            auth['username'], auth['password'], token_new, token_refresh, time.time()
        ))
