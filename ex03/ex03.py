''' Classe Retangulo:Crie uma classe que modele um retangulo:
a.Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b.Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c.Crie  um  programa  que  utilize  esta  classe.  Ele  deve  pedir  ao  usuário  que  informe  as  medidades  de  um  local.
Depois,  deve  criar  um  objeto  com  as  medidas  e  calcular  a quantidade de pisos e de rodapés necessárias para o local.'''

from math import ceil


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (self.base*2) + (self.altura*2)

    def qntd_pisos(self):
        x = (self.calcular_area() / 0.36) * 0.1
        return ceil(x + (self.calcular_area() / 0.36))

    def rodape(self):
        return ceil(self.calcular_perimetro() / 0.6)

    @property
    def mostrar_medidas(self):
        return print(f'Base: {self.base}\nAltura: {self.altura}')

    mostrar_medidas.setter
    def alterar_base(self, base):
        self.base = base
    def alterar_altura(self, altura):
        self.altura = altura

class Informativos:
    def __init__(self):
        print('=*' * 30)
        print('Calculos com base em;\n'
                 'Pisos de 60cm x 60cm\n'
                 'Rodapés de 10cm x 10cm')


def main():
    base = float(input('Base: '))
    altura = float(input('Altura: '))
    dados = Retangulo(base, altura)

    print('Área: {}'.format(dados.calcular_area()))
    print('Perímetro: {}'.format(dados.calcular_perimetro()))
    print(f'Pisos necessario: {dados.qntd_pisos()}')
    print(f'Rodapés necessário: {dados.rodape()}')

    Informativos()

if __name__ == "__main__":
    main()
