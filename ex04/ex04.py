''' Classe Pessoa: Crie uma classe que modele uma pessoa:
a.Atributos: nome, idade, peso e altura
b.Métodos: Envelhercer, engordar, emagrecer, crescer.Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm '''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        return self.idade + anos

    def engordar(self, kg):
        return self.peso + kg

    def emagrecer(self, emagrece):
        return self.peso - emagrece

    def crescer(self, aumento):
        if self.idade + aumento < 21:
            self.altura = self.altura + (aumento * 0.05)
