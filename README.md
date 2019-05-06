# django-mintlog
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![CircleCI](https://circleci.com/gh/jihoonerd/mintlog.svg?style=svg)](https://circleci.com/gh/jihoonerd/mintlog)

## Demo Site
You can see working demo site at [here](https://jihoon.me).

## Description
Django based personal blog template

Mintlog is for people who want to operate django-based blog without knowing django. Mintlog is primarily specialized for managing blog postings especially written in Markdown with scientific & engineering contents.

![Home Screen](./images/home.jpg)

### Features
* Markdown Posting
* Inline Image Uploading
* Tagging
* Mathjax

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
$ pipenv run "python manage.py makemigrations blog portfolio"
$ pipenv run "python manage.py migrate"
```

Running local server:
```bash
$ pipenv run "python manage.py runserver"
```
