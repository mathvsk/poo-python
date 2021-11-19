# Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material.
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    @property
    def mostraCor(self):
        return self.cor

    def set_trocaCor(self, cor_nova):
        self.cor = cor_nova