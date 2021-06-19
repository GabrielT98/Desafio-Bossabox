from typing import List

class Ferramenta():
    def __init__(self,id :int,nome: str,link: str,descricao:str,tags: List):
        self.__id = id
        self.__nome = nome
        self.__link = link
        self.__descricao = descricao
        self.__tags = tags

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_link(self):
        return self.__link
    def get_descricao(self):
        return self.__descricao
    def get_tags(self):
        return self.__tags