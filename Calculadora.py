# Criando uma classe/ Subtipo de OBJECT: HERDA TODAS AS CARACTERÍSTICAS DE OBJECT

class Calculadora(object):

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def definevalores(self,a,b):
        self.a = a
        self.b = b


    def soma(self):
        return self.a + self.b;

