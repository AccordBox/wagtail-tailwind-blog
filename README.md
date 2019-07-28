## Introduction

[![Build Status](https://travis-ci.org/AccordBox/wagtail-bootstrap-blog.svg?branch=master)](https://travis-ci.org/AccordBox/wagtail-bootstrap-blog)

This project is developed exclusively for Wagtail Tutorial [Build Blog With Wagtail CMS](https://www.accordbox.com/blog/wagtail-tutorials/), which shows people how to create a Wagtail blog using Bootstrap step by step. You can also import it into your Django project to quickly add professional blog function based on Wagtail.

## Project Detail

* Python 3
* Django 2
* Wagtail 2
* Bootstrap 4

## Live Demo

I have deployed a live Wagtail Blog Demo on Heroku, you can check it [Wagtail Blog Live Demo](http://wagtail-bootstrap-blog.accordbox.com/blog/).

The admin page of this live demo is [blog admin](http://wagtail-bootstrap-blog.accordbox.com/admin/pages/4/) , you can use `admin:admin` to login and publish articles as you like.

**The database and media files would be reset after a while, so do not be surprised if your article is gone.**

## Run it in local env

```bash
git clone https://github.com/michael-yin/wagtail-bootstrap-blog.git
cd wagtail-bootstrap-blog
git checkout master

# setup virtualenv
pip install -r requirements.txt

./manage.py runserver
# http://127.0.0.1:8000/blog
# username: admin  password: admin
```

If you have any problem with your Wagtail project you can [contact me](https://www.accordbox.com/contact/)

## ScreenShot

![](https://blog.michaelyin.info/upload/images/wagtail-demo-live-screenshot-bootstrap4.original.jpg)

