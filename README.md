## Introduction

This project is from my book [Build Blog With Wagtail CMS](https://leanpub.com/buildblogwithwagtailcms/)

Other books written by me

* [The Definitive Guide to Next.js and Wagtail](https://leanpub.com/the-definitive-guide-to-nextjs-and-wagtail/)
* [Build SPA with React and Wagtail](https://leanpub.com/react-wagtail)
* [The Definitive Guide to Hotwire and Django](https://leanpub.com/hotwire-django)

## Objective

This book will teach you how to build a modern blog with `Wagtail CMS`

By the end of this course, you will be able to:

1. Understand `Docker` and use `Docker Compose` to do development
1. Use `Tailwind CSS` as style solution, and `Stimulus` as frontend solution.
1. Create blog models to work with Wagtail.
1. Use `PDB` and `Django shell` to debug, test code and check data in terminal.
1. Learn to use `RoutablePage` and add `Date` to the post url.
1. Build `Pagination` component and correctly handle querystring.
1. Make the blog supports writing in `Markdown` and `Latex`.
1. Create contact page using Wagtail `FormBuilder`
1. Build menu, meta tags, sitemap, robots.txt for better SEO.
1. Build comment system based on `django-contrib-comments` which support `Generic Relations`
1. Create Frontend project from `python-webpack-boilerplate` and load compiled CSS and JS in Django template.
1. Use `Tribute.js`, `Axios` to add `Mention` and `Emoji` support to the comment form.
1. Deploy the production app to DigitalOcean

## Tech

* Python 3.10
* Django 4
* Wagtail 4
* Stimulus 3
* Tailwind CSS 3

## How to run on local

```bash
$ git clone https://github.com/AccordBox/wagtail-bootstrap-blog
$ cd wagtail-bootstrap-blog
```

First, let's build frontend assets, please make sure `node` is available.

```bash
$ node -v

# install dependency packages
$ npm install

# launch webpack dev server and keep it running
$ npm run watch
```

You need Docker and Docker Compose and you can install it here [Get Docker](https://docs.docker.com/get-docker/)

```bash
# build and launch app
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

## Screenshot

![](./misc/screenshot.png)
