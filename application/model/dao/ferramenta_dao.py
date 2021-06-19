from application.model.entily.ferrementa import Ferramenta

class FerramentaDAO():
    def __init__(self):
        self.__ferramenta_list = []

    def adicionar_ferramenta(self,ferramenta:Ferramenta):
        self.__ferramenta_list.append(ferramenta)

    def listar_ferramentas(self):
        return self.__ferramenta_list