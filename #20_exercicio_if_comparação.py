print('QUAL É MAIOR? by Kai')

valor_1 = input('Digite o primeiro valor: ')
valor_2 = input('Digite o segundo valor: ')

if valor_1 > valor_2:
    print(f'{valor_1} é maior que {valor_2}.')
elif valor_1 < valor_2:
    print(f'{valor_2} é maior que {valor_1}.')
elif valor_1 == valor_2:
    print(f'{valor_1} é igual a {valor_2}.')
else:
    print('Operação inválida.')