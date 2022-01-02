from flask import Flask, redirect, url_for
from flask import render_template
from flask import Blueprint, render_template
from interact_with_DB import interact_db
from flask import request
from flask import session
import mysql.connector

# Delete_user blueprint definition
Delete_user = Blueprint('Delete_user', __name__, static_folder='static', static_url_path='/Delete_user', template_folder='templates')


# Routes
@Delete_user.route('/Delete_user', methods=['POST'])
def index():
    user_id = request.form['id']
    query = "DELETE FROM  users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')


