import yaml


with open('auth.yml', 'r') as config_fh:
    auth = yaml.load(config_fh)

ghost = {
    'base_url': 'blog.cptmorgan.com',
    'username': auth['username'],
    'password': auth['password']
}

osm = {}
