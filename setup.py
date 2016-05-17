try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'The funniest joke in the world',
    'author': 'Shawnyanwang',
    'url': 'URL to get it at.',
    'download_url': 'https://github.com/shawnyanwang/print_hello113',
    'author_email': 'shawnyanwang@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['print_hello113'],
    'scripts': [],
    'name': 'print_hello113'
}

setup(**config)