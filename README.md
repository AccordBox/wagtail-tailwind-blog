## Introduction

This project is from my book [Build Blog With Wagtail CMS (2.0.0)](https://leanpub.com/buildblogwithwagtailcms/), it will teach you how to build a modern blog with Wagtail CMS

## Highlight features

1. Use `Docker` and `Docker-Compose` to manage infrastructure.
1. Flexible page content with `StreamField`
1. Support writing in `Markdown` and `Latex`
1. Clean comment form which supports `mention` and `emoji`
1. Modern frontend stack: `ES6`, `SCSS`, `Webpack`.

## Tech

* Django 3.1
* Wagtail 2.11
* Webpack 5
* jQuery 3.5.1
* Bootstrap 4.5
* Tribute.js
* Axios

## How to run on local

You need Docker and Docker Compose and you can install it here [Get Docker](https://docs.docker.com/get-docker/)

```bash
$ git clone https://github.com/AccordBox/wagtail-bootstrap-blog
$ cd wagtail-bootstrap-blog
# build and lanch app
$ docker-compose up --build
```

Now open a new terminal to import data and change password.

```bash
$ docker-compose exec web python manage.py load_initial_data
$ docker-compose exec web python manage.py changepassword admin
```

Now you can check on

* [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Demo

The demo is also online if you want to check.

* [Wagtail Blog Demo](http://wagtail-blog.accordbox.com)

## ScreenShot

![](./misc/comment.gif)

