class Medicamento:
    def __init__(
        self,
        nome: str,
        fabricante: str,
        dosagem: str,
        preco: float,
        quantidade: int,
        tipo: str,
        prescricao: str,
        tarjaPreta: str,
    ):
        self.__nome = nome
        self.__fabricante = fabricante
        self.__dosagem = dosagem
        self.__preco = preco
        self.__quantidade = quantidade
        self.__tipo = tipo
        self.__prescricao = prescricao
        self.__tarjaPreta = tarjaPreta

    def atualizar_estoque(self, quantidade, preco):
        self.__nome = self.__nome
        self.__fabricante = self.__fabricante
        self.__dosagem = self.__dosagem
        self.__preco = preco
        self.__quantidade = quantidade
        self.__tipo = self.__tipo
        self.__prescricao = self.__prescricao
        self.__tarjaPreta = self.__tarjaPreta

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_fabricante(self, fabricante):
        self.__fabricante = fabricante

    def get_fabricante(self):
        return self.__fabricante

    def set_dosagem(self, dosagem):
        self.__dosagem = dosagem

    def get_dosagem(self):
        return self.__dosagem

    def set_preco(self, preco):
        self.__preco = preco

    def get_preco(self):
        return self.__preco

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def get_quantidade(self):
        return self.__quantidade

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def set_prescricao(self, prescricao):
        self.__prescricao = prescricao

    def get_prescricao(self):
        return self.__prescricao

    def set_tarjaPreta(self, tarjaPreta):
        self.__tarjaPreta = tarjaPreta

    def get_tarjaPreta(self):
        return self.__tarjaPreta
