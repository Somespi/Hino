from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme_file:
   LONG_DESC = readme_file.read()

setup(
    name='hino',
    version='0.0.483',
    author='Someone',
    author_email='',
    description='unofficial API package for Hino.',
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=["API","hino","unofficial","Hino"],
    url='https://github.com/Somespi/Hino/',
    packages=find_packages(),
    install_requires=['requests'],
    include_package_data=True,
    zip_safe=False,
)
