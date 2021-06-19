from application import app
from flask import Flask, render_template, redirect,url_for

@app.route("/")
def index():
    return render_template("index.html")