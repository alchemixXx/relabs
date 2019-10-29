Scope of technologies:
Python 3
Postgresql

Main task:
Create base web server using Flask / Django 
Connect to database - Postgresql
Create a functionality that goes to github and get list of repositories from author 
(example - https://github.com/python)
using GitHub API (https://developer.github.com/v3/)
You should use GET methods and and receive an json-response data
Store repository information into database.
Feel free to choose the table name.
You should store: 
- “name”, 
- “html_url”,
- “description”,
- “private”,
- “created_at”,
- “watchers” as database columns, other stuff fell free how to store.

Create endpoints:
get the list of all repositories from database
get and individually repo by it’s id (unique id in your database)

Requirements:
use logging
use Exceptions Handling

Advanced:
Use Docker and docker-compose for running app automatically 