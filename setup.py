from distutils.core import setup

req = open('requirements.txt')
requirements = req.readlines()
req.close()
version = __import__('chatterbot').__version__
author = __import__('chatterbot').__author__
author_email = __import__('chatterbot').__email__
setup(
    name = 'ChatterLearning',
    packages = [
        'chatter_learning',
        'chatter_learning.brains',
        'chatter_learning.store_adapters',

    ],
    install_requires= requirements,
    scripts = [],
    version = version,
    description = 'Automatic Chat',
    author = author,
    author_email = author_email,
    url = 'https://github.com/gcaaa31928/ChatterLearningt',
    download_url = 'https://github.com/gcaaa31928/ChatterLearning/releases/tag/v1.0',
    keywords = ['ai', 'chat', 'bot'],
    classifiers = [],
)