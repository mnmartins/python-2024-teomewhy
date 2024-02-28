#Numeros em python:
# 1
# 10.0
# -5
# -7.54

#Booleanos em python:
True
False

#soma = 2 + 2 = 4 -> True

condicao = 12 > 18 #-> False

if condicao:
    print('Isso e verdade.')
else:
    print('Isso nunca vai acontecer.')

#%%

idade = int(input('Entre com a sua idade: '))
cnh = input('Voce tem CNH? [S]sim ou [N]nao')

# == eh case sensitive, sendo assim 
if idade >= 18 and cnh == 'S':
    print('Nada errado por aqui!')
else:
    print('Que pena, ainda nao pode dirigir :(')

condicao = idade >= 18 and cnh == 'S'
print(condicao)

# %%
# tabela verdade de E (AND):
# - so eh verdade quando todas as condicoes sao verdadeiras
print('True e True =', bool(1 * 1))
print('True e False =', bool(1 * 0))
print('False e  True =', bool(0 * 1))
print('False e  False =', bool(0 * 0))

# %%
# tabela verdade de OU (OR):
# - so eh verdade quando todas as condicoes sao verdadeiras
print('True ou True =', bool(1 + 1))
print('True ou False =', bool(1 + 0))
print('False ou  True =', bool(0 + 1))
print('False ou  False =', bool(0 + 0))

#pags 24 e 25 sao para live
#pags 26 a 32 p/ casa

