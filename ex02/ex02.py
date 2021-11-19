# Clastamanho=NoneCrie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    @property
    def retorna_valor(self):
        return self.tamanho

    @retorna_valor.setter
    def novo_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def calcular_area(self):
        return self.tamanho * self.tamanho