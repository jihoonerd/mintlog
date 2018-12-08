# django-mintlog
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![CircleCI](https://circleci.com/gh/jihoonerd/mintlog.svg?style=svg)](https://circleci.com/gh/jihoonerd/mintlog)

## Description
Django based personal blog template
![Home Screen](./images/home.jpg)

## Installation
This project manages environment with [`pipenv`](https://pipenv.readthedocs.io/en/latest/).
```bash
$ pip install pipenv --user
```
Now, you can prepare your environment and install packages simply by:
```bash
$ pipenv install
```

## Running Local Server
For the first launching, DB migration is required:
```bash
$ pipenv run "python manage.py migrate"
$ pipenv run "python manage.py migrate --run--syncdb
```

Running local server:
```bash
$ pipenv run "python manage.py runserver"
```
