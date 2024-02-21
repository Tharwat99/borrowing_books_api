# Borrowing-books-API
Simple API for Borrow Books system for users. The API should allow normal users to view books, borrow books and 
admin user to control book creation, update, and borrowing process.

## Normal Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Tharwat99/borrowing_books_api.git
$ cd borrowing_books_api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
```
in Windows
```sh
$ cd env/Scripts
$ activate
```
or Linux
```sh
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
You should create .env file in api dir and variables inside it:

**Note:** Create a SECRET_KEY value for your app by running the following command at a terminal prompt: python -c 'import secrets; print(secrets.token_hex())'.

```sh
SECRET_KEY = "<put_your_secret_key_here>"
DEBUG = True
# optional parts
# DB_ENGINE='django.db.backends.mysql'
# DB_HOST='staging-db'
# DB_NAME='datalex4ai_db'
# DB_USER='datalex4ai_user'
# DB_PASSWORD='datalex4ai_password'
# DB_PORT=3306
```
Then makemigrations and migrate models to sqlite db or any db you add it to settings:

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
