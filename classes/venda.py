from enum import Enum

class Pagamento(Enum):
    DINHEIRO = "dinheiro"
    PIX = "pix"
    DEBITO = "débito"
    CREDITO = "crédito"

class Venda:
    def __init__(self, itens_comprovante: list, total: float, pagamento: Pagamento):
        self.__pagamento = pagamento
        self.__itens = itens_comprovante
        self.__total = total
    
    def set_pagamento(self, pagamento):
        self.__pagamento = pagamento    

    def get_pagamento(self):
        return self.__pagamento
    
    def set_itens(self, itens):
        self.__itens = itens
        
    def get_comprovante_itens(self):
        return self.__itens
    
    def set_total(self, total):
        self.__total = total 

    def get_total(self):
        return self.__total
    
    def get_itens_para_gravar(self):
        return ", ".join([f"{item['nome']}:{item['qtd']}" for item in self.__itens])