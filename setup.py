import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mbd_cms_template",
    version = "0.0.1",
    author = "Alexandro Blanco",
    author_email = "alex@aait.tech",
    description = ("DJango CMS Template and plugins for Minneapolis Ballet Dancers website"),
    license = "MIT",
    keywords = "MDB django djangocms template plugins",
    url = "https://github.com/ti3r/mbd-cms-template.git",
    packages=['mbd_cms_template', 'tests'],
    long_description='Template for the Minneapolis Ballet Dancers organization',
    classifiers=[
    ],
)