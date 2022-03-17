import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-admin-commands',
    version='0.92',
    packages=['admincommands', 'admincommands.migrations'],
    description='Allow running Django management commands at the ease of your admin panel',
    long_description=README,
    author='Eralp Bayraktar',
    author_email='imeralpb@gmail.com',
    url='https://github.com/EralpB/django-admin-commands/',
    license='MIT',
    install_requires=[
        'Django>=1.6'
    ]
)