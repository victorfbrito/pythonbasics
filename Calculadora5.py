from Calculadora3 import Pessoa
class Pessoajuridica(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.CNPJ= ""

    def atualizadados(self, dicdados):
        Pessoa.atualizadados(self,dicdados)
        self.CNPJ = dicdados['CNPJ']

    def retornadados(self):
        return Pessoa.retornadados(self) + ' CNPJ %s ' %[self.CNPJ]

