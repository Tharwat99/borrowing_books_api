# Borrowing-books-API
Simple API for Borrow Books system for users. The API should allow normal users to view books, borrow books and 
admin user to control book creation, update, and borrowing process.

## Normal Setup

The first thing to do is to clone the repository:

```sh
$ git https://github.com/Tharwat99/borrowing_books_api.git
$ cd borrowing_books_api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Then makemigrations and migrate models to sqlite db:

```sh
(env)$ python manage.py makemigrations 
(env)$ python manage.py migrate
```

Once `pip` has finished downloading the dependencies:

## Tests

To run the tests:
```sh
(env)$ pytest
```

## Run Server

```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Docker Setup

build docker-compose file
```sh
$ docker-compose up --build
```
## Tests

To run the tests:
```sh
(env)$ docker-compose run backend sh -c "pytest"
```
