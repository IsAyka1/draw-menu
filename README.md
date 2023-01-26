# draw_menu
Django template tag which draws a tree-like menu in your page

## How to use
* install requirements from 'menu/'
```commandline
pip install -r requirements.txt
```
* create superuser
```commandline
su postgres -c psql postgres
psql-# ALTER USER admin WITH PASSWORD 'password';
```
* create db
```commandline
psql-# CREATE DATABASE db_menu WITH OWNER admin;
```
* create migrations from 'menu/test_project/'
```commandline
python3 manage.py makemigrations
python3 manage.py migrate
```
* load templatetags in your page
```commandline
{% load draw_menu %}
```
* draw your menu by name  in your page
```commandline
<div class="some-class">
    {% draw_menu 'main_menu' %}
</div>
```
You can use not-root 'name' then all menu will be drawn and node with 'name' will be **selected**
* run your project
```commandline
python3 manage.py runserver
```