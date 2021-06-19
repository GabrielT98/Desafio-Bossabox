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
    ferramenta = Ferramenta(id,nome,link,descricao,tags)
    ferramenta_dao.adicionar_ferramenta(ferramenta)

    return render_template("index.html", list_ferramentas=list_ferramentas)
@app.route("/remover/<id>")
def remover(id: int):
    for ferramenta in list_ferramentas:
        if ferramenta.get_id() == int(id):
            list_ferramentas.remove(ferramenta)
            return render_template("index.html", list_ferramentas=list_ferramentas)

@app.route("/buscar")
def buscar():
    lista_ferramenta_filtrada= []

    if request.form.getlist('search') == []:
        palavra_chave = request.args.get('palavra-chave')
        for ferramenta in list_ferramentas:

            if palavra_chave in ferramenta.get_nome() or palavra_chave in ferramenta.get_descricao() or palavra_chave in ferramenta.get_tags():
                lista_ferramenta_filtrada.append(ferramenta)
        return render_template("index.html",list_ferramentas = lista_ferramenta_filtrada)

    else:
        palavra_chave = request.args.get('palavra_chave')
        for ferramenta in list_ferramentas:
            if palavra_chave in ferramenta.get_tags():
                lista_ferramenta_filtrada.append(ferramenta)

        return render_template("index.html",list_ferramentas = lista_ferramenta_filtrada)



