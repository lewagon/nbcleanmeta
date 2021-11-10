
import os

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="nbcleanmeta",
      version="0.2.0",
      description="Le Wagon notebook metadata cleaner tool",
      packages=find_packages(),
      install_requires=requirements,
      scripts=[os.path.join("scripts", "nbcleanmeta")])
