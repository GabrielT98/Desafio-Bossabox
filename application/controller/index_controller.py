from application import app
from flask import Flask, render_template, redirect,url_for

from application.model.dao.ferramenta_dao import FerramentaDAO

ferramenta_dao = FerramentaDAO()
list_ferramentas = ferramenta_dao.listar_ferramentas()
@app.route("/")
def index():
    return render_template("index.html",list_ferramentas = list_ferramentas)

@app.route("/inserir")