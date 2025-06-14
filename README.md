# django_proj

## Created this python project that uses Django framework.

1. install python
   `pip install pipenv`

install django using pipenv to save in virtual env
`pip env install django`

launch virtual environment. always run this to make web app run seamlessly
`pipenv shell`

create a project folder
`django-admin startproject <nameofyourproject>`

create an app folder
`python manage.py startapp <nameofyourapp>`

use this code throughout
`python manage.py <command>`

run the server
`python manage.py runserver`

adding and updating models.py, always run this code to process and update the database sqlite3
`python manage.py makemigrations`
`python manage.py migrate`

### To access Django admin panel

1. create superuser
   `python manage.py createsuperuser`
2. access admin panel by adding '/admin' at the end of URL

- Django by default uses SQL Lite, a lightweight databse

### MVT

1. Model - managing data. it is the database
2. View - take user request and process. deals with logic part of application (view.py file)
   - class-based view
   - function-based view
   * urls.py - url mapping. Creates a path to access the link from views.py
3. Template - HTML markup, dynamic components. template for user interface

### Create a MYSQL Database

1. Install MYSQL
   `pip install mysqlclient`
2. Access MySQL
   `mysql -u root -p`

- if you can't remember your password. Rest MySQL Root Password
  a. Stop MySQL `brew services stop mysql`
  b. Start MySQL in safe mode:
  `mysqld_safe --skip-grant-tables &`
  c. Open new terminal window and login as root
  `mysql -u root`
  d. Change the root password
  `FLUSH PRIVILEGES;`
  `ALTER USER 'root'@'localhost' IDENTIFIED BY 'newpassword';`
  e. Login with your new password

3. Create your DB
   `create database <name of db>;`
4. To use the database
   `use <nameofdb>'`
5. To see that db changed
   `show tables;`
6. To exit MySQL
   `\q`

### Configure MySql in Django

1. Install driver inside VS Code
   `pip install mysqlclient`
2. Adjust DB list in settings.py under project folder
   - Go to line DATABASE
   - Update Engine and Name
   - Add User and Password

### File directory

project/
├── myfirstproj/
│ └── templates
│ └── migrations
│ └── static/
│ │ └── css
│ │ └── img
└── myfirstapp/
│ └── settings.py
│ └── urls.py
└── manage.py
