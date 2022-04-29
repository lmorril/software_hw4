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


# React Native App - Instructions for MAC OS

## 0. Installation
To run this project, you need to have Python 3+ and npm (from Node.js) installed.
Then, clone this project with the following command:
```bash
git clone https://github.com/lmorril/assignment3.git <local directory of your choice>
```

## 1. Start Virtual Enviroment
In your terminal, change the current working directory to "local directory of your choice" and run:
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

## 3. Run the Frontend

### Dependencies
With the backend running, change the working directory as follows (you may open another terminal):
```bash
cd <root directory of the project>
cd frontend/my-app
```
Everything required should be provided as specified in package.json already,
but just in case, here are the commands to check if we have all the node module dependencies:
```bash
npm install
```

### Get Started
Now, type the following command in the same terminal to fire up the React Native app:
```bash
npm start
```
Then, follow the instruction in the terminal to either open Android, iOS or web simulator.

### Using the App - Core Features:

### On Home screen
  - Table of viewable ratings. Click on edit or delete to change the entries.

     - Edit: Re-enter the id and username, then change to the rating you want. After clicking save, reload the page to see your edited entry in the table
     - Delete: click delete to remove entry from the database

  - Add your new rating by enter your id, username, song, artist, and rating to create a new rating in the app. Note that you can only add ratings that ate 1-5 and if you enter the correct ID.

### On Add User screen

  - Search the database for all entries of a certain artist. Type in the artist name and find past ratings for each of their songs

### On Stats screen

  - Get summary stats of the ratings. Provided is average rating across all songs, average rating by artist, and average rating by song.

