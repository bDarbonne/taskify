# Taskify
Used to make writing python tasks easier so that you can focus on getting stuff done. Taskify takes care of implementation boiler-plate and provides a more generic
interface for performing tasks.

## Installation
```bash
$ pip install taskify
```

## Usage
```python
from taskify import greet

# output the greeting 'hello bob'
greet('Bob')

```

## Development
To install taskify, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
$ pip install -e .[dev]

# is for Apps being deployed on machines you control
# uses fixed version numbers, ex: requests=1.5.0
$ pip freeze > requirements.txt
```

## Source Distribution
```bash
$ python setup.py sdist
```

## Check Manifest
```bash
$ pip install check-manifest

$ check-manifest --create

$ git add MANIFEST.in
```

## Build It
```bash
$ python setup.py bdist_wheel sdist

$ ls dist/
```

## Push To PyPI
```bash
$ pip install twine

$ twine upload dist/*
```