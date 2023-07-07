## Introduction

This open source project is for my book [Build Blog With Wagtail CMS](https://leanpub.com/buildblogwithwagtailcms/)

**You can support my work by purchasing the ebook**

Other books written by me

* [The Definitive Guide to Next.js and Wagtail](https://leanpub.com/the-definitive-guide-to-nextjs-and-wagtail/)
* [Build SPA with React and Wagtail](https://leanpub.com/react-wagtail)
* [The Definitive Guide to Hotwire and Django](https://leanpub.com/hotwire-django)

## Objective

This book will teach you how to build a modern blog with `Wagtail CMS`

By the end of this course, you will be able to:

1. Understand `Docker` and use `Docker Compose` to do development
1. Use `python-webpack-boilerplate` to jump start frontend project bundled by Webpack.  
1. Install `Tailwind CSS` as the style solution.
1. Install `Stimulus`, understand how it works and write Stimulus controllers.
1. Learn how `Dark Mode` works in Tailwind CSS and use Stimulus controller to toggle the dark mode.
1. Understand the benefit of the healthy Stimulus ecosystem by reusing 3-party Stimulus controller.
1. Create blog models to work with Wagtail.
1. Use `PDB` and `Django shell` to debug, test code and check data in terminal.
1. Learn to use `RoutablePage` and add `Date` to the post url.
1. Build `Pagination` component and correctly handle querystring.
1. Make the blog supports writing in `Markdown` and `Latex`.
1. Create contact page using Wagtail `FormBuilder`
1. Build menu, meta tags, sitemap, robots.txt for better SEO.
1. Build comment system based on `django-contrib-comments` which support `Generic Relations`
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
$ git clone https://github.com/AccordBox/wagtail-tailwind-blog
$ cd wagtail-tailwind-site
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




## M1 Mac

### update browserlist 
npx browserslist@latest --update-db


### install rosetta
softwareupdate --install-rosetta

### tell docker to build and run on amd64 platform
export DOCKER_DEFAULT_PLATFORM=linux/amd64
docker-compose build
docker-compose up
### Make sure node version is:
v18.16.0

## Dumping Data

docker-compose run --rm web python manage.py dumpdata --natural-foreign --indent 2 -e auth.permission -e contenttypes -e wagtailcore.GroupCollectionPermission -e wagtailcore.revision -e wagtailimages.rendition -e sessions -e wagtailsearch.indexentry -e wagtailcore.pagesubscription -e wagtailcore.modellogentry -e wagtailcore.pagelogentry > wagtail_app/site/fixtures/sitedemo2.json
prettier --write wagtail_app/site/fixtures/sitedemo2.json