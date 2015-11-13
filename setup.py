from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.8.4',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='YourAppName',
      version='1.0',
      description='Simply Res',
      author='Ketaki Rao',
      author_email='ketakisrao@outlook.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

