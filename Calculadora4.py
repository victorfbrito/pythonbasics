from Calculadora3 import Pessoa

class Pessoafisica(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.CPF = ''

    def atualizadados(self, dicdados):
        Pessoa.atualizadados(self,dicdados)
        self.CPF = dicdados['CPF']

    def retornadados(self):
        return Pessoa.retornadados(self) + 'CPF %s' % (self.CPF)