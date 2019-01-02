## Introduction

[![Build Status](https://travis-ci.org/AccordBox/wagtail-bootstrap-blog.svg?branch=master)](https://travis-ci.org/AccordBox/wagtail-bootstrap-blog)

This project is developed exclusively for Wagtail Tutorial [Build Blog With Wagtail CMS](https://blog.michaelyin.info/wagtail-tutorials/?utm_source=github&utm_medium=website&utm_campaign=wagtail_tuto), which shows people how to create a Wagtail blog using Bootstrap step by step. You can also import it into your Django project to quickly add professional blog function based on Wagtail.

## Project Detail

* Python 3
* Django 2
* Wagtail 2
* Bootstrap 4

## Live Demo

I have deployed a live Wagtail Blog Demo on my Linode VPS, you can check it [Wagtail Blog Live Demo](http://wagtail.michaelyin.info/blog/).

The admin page of this live demo is [blog admin](http://wagtail.michaelyin.info/admin/pages/4/) , you can use `admin:admin` to login and publish articles as you like. **To avoid somebody sends spam, the database would be reset every half hour, so do not be surprised if your article is gone.**

You can check this page for more detail. [Wagtail Blog Demo is now available](https://blog.michaelyin.info/2018/02/01/wagtail-blog-demo-now-available/)

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

If you have any problem with your Wagtail project you can [contact me](https://blog.michaelyin.info/about/#contact)

## ScreenShot

![](https://blog.michaelyin.info/upload/images/wagtail-demo-live-screenshot-bootstrap4.original.jpg)

