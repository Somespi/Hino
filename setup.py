from setuptools import setup, find_packages
import os

LONG_DESC = open('./README.md', 'r').read()


setup(
    name='hino',
    version='0.0.48',
    author='Someone',
    author_email='',
    description='unofficial API package for Hino.',
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=["API","hino","unofficial","Hino"],
    url='https://github.com/Somespi/Hino/',
    packages=find_packages(),
    scripts=[],
    install_requires=['requests'],
    include_package_data=True,
    zip_safe=False,
)
