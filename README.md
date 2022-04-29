# software_hw4
Assignment 4 in COMP 333 at Wesleyan University


# Noah - Deployment
backend - https://music-mobile.herokuapp.com/admin/

frontend - https://music-mobile-1167e.web.app/

## Deployed APP
When you edit you must reload to see it update.

Login only works when you use 
    username: luke
    password: 123

In order to edit or enter a rating you must use 
    username: luke
unless you manualy add a user with the admin page.


# React Native 

## Django Backend Installation
To run this project, you need to have Python 3+ and npm (from Node.js) installed.

## 1. Start Virtual Enviroment
In your terminal, change the current working directory to <local directory of your choice> and run:
```bash
source django-react/bin/activate
```

## 2. Run the Backend
```bash
cd backend
python3 manage.py runserver
```

### View the APIs:
For the database of Users visit url:
http://127.0.0.1:8000/api/users/

For Ratings:
http://127.0.0.1:8000/api/ratings/

Here you can do GET/POST requests.

For PUT request go to the ratings url, go to the url above, but put the id of the entry to be changed at the end, for example:
http://127.0.0.1:8000/api/ratings/1/

### Dependencies

The dependencies should be installed on the virtual environment, but just in case here's what you need for the backend:
```bash
pip3 install djangorestFramework django-cors-headers
```