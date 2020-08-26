class Pessoa(object):
    def __init__(self):
        self.nome = ''
        self.sobrenome = ''
        self.idade = 0
        self.datanascimento = ''

    def atualizadados(self, dicdados):
        self.nome = dicdados['nome']
        self.sobrenome = dicdados['sobrenome']
        self.idade = dicdados['idade']
        self.datanascimento = dicdados['datanascimento']

    def retornadados(self):
        return 'A pessoa %s %s de %d anos de idade nascida em %s foi atualizada com sucesso ' %(self.nome, self.sobrenome, self.idade, self.datanascimento)