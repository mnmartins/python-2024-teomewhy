#%%

#Trabalhando com estruturas de condicao
idade = int(input('Digite a sua idade: '))

# No python nao tem parenteses para a condicao. 
# Caso a condicao seja verdadeira, os dois pontos apos a condicao
#definem que tudo o que estiver com 4 espacos a direita(identado) 
#sera executado(os espacos sao o que definem o que sera executado
# a seguir, semelhante as chaves do Java)

if idade > 80:    print('Cuidado com a saude, voce ja tem certa idade!') #nesse modelo so posso colocar uma execucao de uma linha

elif idade >= 18:
    print('Voce e maior de idade =D\nBeba o que quiser.')

else:
    print('Voce e muito jovem :D')
    print('Beba agua.') # nesse modelo posso ter comandos em varias linhas
# %%
