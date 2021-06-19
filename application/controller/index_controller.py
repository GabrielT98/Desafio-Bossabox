from application import app
from flask import Flask, render_template, redirect,url_for,request

from application.model.dao.ferramenta_dao import FerramentaDAO
from application.model.entily.ferrementa import Ferramenta

ferramenta_dao = FerramentaDAO()
list_ferramentas = ferramenta_dao.listar_ferramentas()
@app.route("/")
def index():
    return render_template("index.html",list_ferramentas = list_ferramentas)

@app.route("/inserir",methods=["POST"])
def inserir():
    id = len(list_ferramentas)+1
    nome = request.form.get('nome',None)
    link = request.form.get('link',None)
    descricao = request.form.get('descricao',None)
    tags = request.form.get('tags',None)
    ferramenta = Ferramenta(id,nome,link,descricao)
    ferramenta.set_tags(tags)
    ferramenta_dao.adicionar_ferramenta(ferramenta)
    return render_template("index.html", list_ferramentas=list_ferramentas)


