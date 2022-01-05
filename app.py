from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session
import mysql.connector

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## assignment10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

## Insert_user
from pages.Insert_user.Insert_user import Insert_user
app.register_blueprint(Insert_user)

## Delete_user
from pages.Delete_user.Delete_user import Delete_user
app.register_blueprint(Delete_user)

## Update_users
from pages.Update_users.Update_users import Update_users
app.register_blueprint(Update_users)


## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

@app.route('/req_frontend')
def req_frontend():
    return render_template('req_frontend.html')

@app.route('/req_backend')
def req_backend():
    return render_template('req_backend.html')

if __name__ == '__main__':
    app.run(debug=True)