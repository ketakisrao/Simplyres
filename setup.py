from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.8.4', 'python-social-auth==0.2.1', 'django-crispy-forms', 'djangorestframework', 'django-registration-redux']

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='SimplyRes!',
      version='1.0',
      description='SimplyReserve!',
      author='Ketaki Rao',
      author_email='ketakisrao@outlook.com',
      url='https://simplyres-ketakisrao.rhcloud.com/',
      install_requires=packages,
)