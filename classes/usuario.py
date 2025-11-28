from enum import Enum


class Papel(Enum):
    FARMACEUTICO = "farmaceutico"
    CAIXA = "caixa"


class Usuario:
    def __init__(self, nome: str, senha: list, papel: Papel):
        self.__nome = nome
        self.__senha = senha
        self.__papel = papel

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_senha(self, senha):
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def set_papel(self, papel):
        self.__papel = papel

    def get_papel(self):
        return self.__papel
