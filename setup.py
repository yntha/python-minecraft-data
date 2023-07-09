import os

from distutils.core import setup

from setuptools import find_packages


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('minecraft_data/data/data')
long_desc = "Failed to load README.rst"

with open('README.rst', 'r') as readme_fobj:
  long_desc = readme_fobj.read()

setup(
    name='minecraft_data',
    description='Provide easy access to minecraft data in python',
    license='MIT',
    long_description=long_desc,
    version='3.39.0',
    maintainer='Anthy',
    maintainer_email='vito@gamberini.email',
    url='https://github.com/yntha/python-minecraft-data',
    packages=find_packages(),
    package_data={'minecraft_data': extra_files},
    install_requires=[],
    keywords=['minecraft'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
