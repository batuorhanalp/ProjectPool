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
  
Each time you start developing or running, make sure you run the following command:

    source venv/bin/activate

First time installation (and whenever you change anyhing in the models, also make sure that issue `cd project_pool` if you're not in the development folder):

    python manage.py syncdb

To run the project issue following commands (`cd project_pool` if you're not in the development folder):

    python manage.py runserver_plus

Visit `http://localhost:8000/` on your browser. You have run the project in development environment.

Deployment
==========

@Todo
