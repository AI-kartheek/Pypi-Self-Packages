from setuptools import setup, find_packages

VERSION='0.1'

classifiers = ['Operating System :: Microsoft :: Windows :: Windows 10',
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python :: 3']

setup(name='Custom_sklearn',
      version=VERSION,
      description='just sample only',
      long_description = open("README.md", "r", encoding="utf-8").read() + '\n\n' + open("CHANGELOG.txt", "r", encoding="utf-8").read(),
      long_description_content_type="text/markdown",
      url = "https://github.com/AI-kartheek/Pypi-Self-Packages/KarthiSource",
      author='Kartheek07',
      author_email = 'ai07kartheek@gmail.com',
      License = 'MIT',
      classifiers = classifiers,
      packages= find_packages(),
      python_requires = '>=3.6')