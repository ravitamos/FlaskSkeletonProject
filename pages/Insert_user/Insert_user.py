from flask import Flask, redirect, url_for
from flask import render_template
from flask import Blueprint, render_template
from interact_with_DB import interact_db
from flask import request
from flask import session
import mysql.connector

# Insert_user blueprint definition
Insert_user = Blueprint('Insert_user', __name__, static_folder='static', static_url_path='/Insert_user', template_folder='templates')


# Routes
@Insert_user.route('/Insert_user', methods=['POST'])
def index():
    #get the data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    #insert to db
    query = "INSERT INTO users(name, email, password) values ('%s','%s','%s')" % (name, email, password)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')
