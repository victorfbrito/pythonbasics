
#IMPORTA UMA CLASSE DO OUTRO ARQUIVO

from Calculadora import Calculadora
from Calculadora3 import Pessoa
from Calculadora4 import Pessoafisica
from Calculadora5 import Pessoajuridica

#FUNCAO DA CALCULADORA 1

calculadora = Calculadora(1,2)
calculadora.definevalores(1,2)
print(calculadora.soma())

# FUNCAO DA CALCULADORA 3

pessoa = Pessoa()
pessoa.atualizadados({'nome': 'Victor', 'sobrenome': 'França', 'idade': 20, 'datanascimento': '2013-23-02'})
print(pessoa.retornadados())

#FUNCAO DA CALCULADORA 4

pessoafisica = Pessoafisica()
pessoafisica.atualizadados({'nome':'José', 'sobrenome':'Bezerra','idade':25,'datanascimento':'1994-04-23','CPF':'46432.44.59-34'})
print(pessoafisica.retornadados())

#CALCULADORA 5

pessoajuridica = Pessoajuridica()
pessoajuridica.atualizadados({'nome':'Empresa', 'sobrenome':'do José','idade':128,'datanascimento':'1912-09-23','CNPJ':'11.222.222.2222/0111-22'})
print(pessoajuridica.retornadados())