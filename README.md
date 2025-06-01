# django_proj

Created this python project that uses Django framework.

install python
`pip install pipenv`

install django using pipenv to save in virtual env
`pip env install django`

launch virtual environment
`pipenv shell`

use this code throughout
`python manage.py <command>`

create an app in django
start project
`django-admin startproject <nameofyourproject>`

MVT

1. Model - managing data. it is the database
2. View - take user request and process. deals with logic part of application (view.py file)
   - class-based view
   - function-based view
   * urls.py - url mapping. Creates a path to access the link from views.py
3. Template - HTML markup, dynamic components. template for user interface

File directory
Project Root Folder
|-- app folder
|--|-- views.py (logic part)
|--|-- urls.py (map url)
|-- project app folder
|--|-- urls.py (assign url set on app level)
|--|-- settings.py (add the app under INSTALLED_APPS)
