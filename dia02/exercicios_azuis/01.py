#%%
# Exercicio 1:
# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

opcao = input('Voce gostaria de uma garrafa de agua mineral ou com gas? [mineral/gas]: ')

if opcao == 'mineral':
    print('Voce me deve R$1,50.')
elif opcao == 'gas':
    print('Voce me deve R$2,50.')
else:
    ('Faca uma escolha valida, por favor!')
