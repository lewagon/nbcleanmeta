
from setuptools import setup, find_packages

import os

with open("requirements.txt") as f:
    requirements = [c.strip() for c in f.readlines()]

setup(name="nbcleanmeta",
      version="0.2.0",
      description="Le Wagon notebook metadata cleaner tool",
      url="https://github.com/lewagon/nbcleanmeta/",
      author="Sébastien Saunier",
      author_email="seb@lewagon.org",
      packages=find_packages(),
      install_requires=requirements,
      scripts=[os.path.join("scripts", "nbcleanmeta")])
