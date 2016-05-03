# Django_Blog( Blog using Django )
If you want to setup Django 1.9, down you will fine everything that will make your life ease to start.

## Installation
  1. install python
  2. install pip
  3. install virtualenv
  4. install Django

  Code for linux(Ubuntu):
  ```bash
    sudo apt-get update

    sudo apt-get install python-pip python-dev build-essential

    sudo pip install virtualenv virtualenvwrapper

    sudo pip install --upgrade pip

  ```

## Setup the project
  1. Make new project
  2. sdf

```bash

    mkdir blog
    cd blog
    virtualenv env # for using python 3 "virtualenv -p /usr/bin/python3"
    srouce env/bin/activate
    pip install django

  ```

  > to check the version of Django that you use:
  ```bash
  pip freeze
  ```

## Create the project
  ```bash
  django-admin startproject mysite
  cd mysite
  ./manage.py startapp blog # or python manage.py startapp blog
  ```
  ### Things I have to add
  > 1. Install the name of the app to the ./mysite/settings under the variable INSTALLED_APPS

  > 2. add urls.py to the new application

  >3. include the urls.py of the new app to ./mysite/urls.py
