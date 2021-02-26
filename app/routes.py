from app import app, db
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/12wk')
def program():
    return render_template('12wk.html')