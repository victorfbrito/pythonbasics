def func(x):
    return x**3

print (func(4))

funclambda = lambda x: x**3

print (funclambda(4))
def f(x,y,z):
    return x+y+z
print (f(1,2,3))

ff = lambda x,y,z: x+y+z
print(ff(1,2,3))
l = lambda a = "oi ", b = "tudo ", c = "bem?" : a+b+c
print(l())

##

def boasvindas():
    titulo = "Senhor"
    nome = (lambda x: titulo + ' ' + x)
    return nome

cboasvindas = boasvindas()
print (cboasvindas("Victor França"))

##

lista = [lambda x:x**2,
         lambda x:x**3,
         lambda x:x**4]
for item in lista:
    print(item(3))

def f1(x):
    return x**2
def f2(x):
    return x**3
def f3(x):
    return x**4

lista1=[f1,f2,f3]

for f in lista1:
    print (f(3))

##
#x = int(input("Diga o número que deseja calcular:"))
#key = str(input('Diga quadrado, cubo ou quarta'))
x = 3
key = 'quadrado'
result = {'quadrado':f1,'cubo':f2,'quarta':f3}[key](x)
print (result)

##
Qualovalorminimo = lambda x,y: x if x < y else y
print(Qualovalorminimo(10,20))


import sys

##Contagem dos caracteres dos membros da lista

#método 1

nomeCompleto = lambda x: list(map(sys.stdout.write, x))
funcaoNome = nomeCompleto(["Fulano",'de','tal'])

#método 2

print(funcaoNome)
nomeCompleto2 = lambda x: [sys.stdout.write(a) for a in x]
funcaoNome2 = nomeCompleto2(['Fulano','de','tal'])
print(funcaoNome2)

def acao(x):
    return (lambda novox: x + novox)

resposta = acao(2)

print(resposta)
print(resposta(3))

acao2 = (lambda x: (lambda novox:x + novox))

resposta2 = acao2(3)(5)
print(resposta2)

##

usuariodatanasc = [
    ('Rafael','Pizza', 30),
    ('Victor','França', 20),
    ('Caue','Chinaglia', 22)
]

print(usuariodatanasc)
#Ordenar por idade
print(sorted(usuariodatanasc,key = lambda variavel : variavel[2] ))
#ordenar por sobrenome
print(sorted(usuariodatanasc,key = lambda variavel : variavel[1] ))
#ordenar por nome
print(sorted(usuariodatanasc,key = lambda variavel : variavel[0] ))