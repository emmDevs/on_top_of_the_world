# on_top_of_the_world

<b>THE BRIEF</b>

Travel Bucket List
Build an app to track someone's travel adventures.

MVP:
The app should allow the user to track countries and cities they want to visit and those they have visited.
The user should be able to create and edit countries
Each country should have one or more cities to visit
The user should be able to create and delete entries for cities
The app should allow the user to mark destinations as visited or still to see

Extensions:
Anything else you would like to add

<b>RUNNING INSTRUCTIONS</b>

You will need to import the library, psycopg2, to allow us to make a connection to a database
and execute a prepared SQL statement on that database

To import psycopg2 type the following command into the Terminal:

<b>pip3 install psycopg2</b>

You will then need to type the following command into the Terminal to create the database and tables and populate them;

<ul>
<li><b>createdb top_of_the_world</b></li>
<li><b>psql -d top_of_the_world -f db/top_of_the_world.sql</b></li>
<li><b>python3 console.py</b></li>
</ul>

to view on localhost:5000 
type <b>flask run</b> into the Terminal

<b>TECHNOLOGIES USED</b>

This app has been built using 
- PSQL
- psycopg2
- Flask
- Python
- HTML
- CSS
