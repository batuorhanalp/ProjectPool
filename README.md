=====================
Karbonat Fikir Havuzu
=====================

Explanation will come here

Installation
============

Install virtualenv if it's not installed before

    pip install virtualenv

Use following to set up the project

    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements/local.txt 

Running The Project
===================
  
Make sure that mongodb is running.

    mongod

To run the project issue following commands:

    cd project_pool
    python manage.py runserver_plus

Visit `http://localhost:8000/` on your browser. You have run the project in development environment.

Deployment
==========

@Todo
