import yaml


with open('auth.yml', 'r') as auth_fh:
    auth = yaml.load(auth_fh)

ghost = {
    'base_url': 'blog.cptmorgan.com',
    'username': auth['username'],
    'password': auth['password'],
    'token': auth['token']
}

osm = {}


def update_token(token_new):
    with open('auth.yml', 'w') as auth_fh:
        auth_fh.write('---\nusername: {0}\npassword: {1}\ntoken: {2}\n'.format(
            auth['username'], auth['password'], token_new
        ))
