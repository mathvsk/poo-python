'''Classe  Conta  Corrente:Crie  uma  classe  para  implementar  umaconta  corrente.  A  classe  deve  possuir  os  seguintes
atributos:  número  da  conta,  nome  do  correntista  e  saldo. Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios'''

class Conta:
    def __init__(self, numero, nome, saldo=0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo

    def get_mostrarNome(self):
        return self.__nome

    def set_alteraNome(self, novo_nome):
        self.__nome = novo_nome
        return

    def deposito(self, depositar):
        self.__saldo += depositar

    def sacar(self, sacar):
        self.__saldo -= sacar