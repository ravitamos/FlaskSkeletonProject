from flask import Flask, redirect, url_for
from flask import render_template
from flask import Blueprint, render_template
from interact_with_DB import interact_db
from flask import request
from flask import session
import mysql.connector

# Update_users blueprint definition
Update_users = Blueprint('Update_users', __name__, static_folder='static', static_url_path='/Update_users', template_folder='templates')


# Routes
@Update_users.route('/Update_users',methods=['POST'])
def index():
    user_id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    query = "UPDATE users SET name='%s',email='%s' WHERE id='%s'" % (name,email,user_id)
    interact_db(query=query, query_type='commit')
    return render_template('assignment10.html')
