# Step by step

This is a clone of the website instructables, where you can post your own projects or search for projects made by others.

Live site: https://step-by-step-app.herokuapp.com/

## Getting started

To view and use this application, you can either navigate to the live site(https://step-by-step-app.herokuapp.com/) and login as a new or demo user, or download the project locally:

1. Clone this repository https://github.com/Noslepr/Python-group-project.git

   ```bash
   git clone https://github.com/appacademy-starters/python-project-starter.git
   ```

2. CD into the /app directory and install dependencies pipenv install

3. CD into the /react-app directory and install dependencies npm install

4. Create a .env file based on the .env.example given

5. Create a user in psql based on your .env DATABASE_URL app_name
psql -c "CREATE USER PASSWORD '' CREATEDB"

6. Create a databse in psql based on your.env DATABASE_URL app_db_name

7. Start your shell, migrate your database, seed your database, and run the flask app
pipenv shell

flask db upgrade

flask seed all

flask run

8. Open another terminal and change directory into /react-app and run the React app npm start

## Screenshots
 Homepage
 ![image](https://user-images.githubusercontent.com/86488501/162483426-72aa9d96-142c-4146-801a-d553b0b0e4c8.png)

   
## Tech Stack

Client: JavaScript, NodeJS, React, Redux

Server: PostgreSQL, Python, Flask, SQLAlchemy
