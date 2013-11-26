from flask import Blueprint, redirect, url_for


mod = Blueprint('main', __name__, url_prefix='/')

@mod.route('/')
def home():
    return redirect(url_for('static', filename='index.html/'))
