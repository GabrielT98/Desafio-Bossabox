from typing import List

class Ferramenta():
    def __init__(self,nome: str,link: str,descricao:str):
        self.__nome = nome
        self.__link = link
        self.__descricao = descricao
        self.__tags = None

    def set_tags(self,tags:List):
        self.__tags = tags
    def get_nome(self):
        return self.__nome
    def get_link(self):
        return self.__link
    def get_descricao(self):
        return self.__descricao
    def get_tags(self):
        return self.__tags