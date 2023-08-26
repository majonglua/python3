# 'if', 'elif' e 'else' representam 'se, 'se não se' e se não'. Eles abrem di-
# versas possibilidades no  fluxo do código, como podemos aplicar no código da
# aula anterior.

valor_1 = input('Digite o primeiro valor: ')
valor_2 = input('Digite o segundo valor: ')
operacao = input('Digite qual será a operação: ')

if operacao == 'Soma':
    resultado = int(valor_1) + int(valor_2) 
    print(f'O resultado de {valor_1} + {valor_2} é {resultado}')
elif operacao == 'Multiplicação':
    resultado = int(valor_1) * int(valor_2) 
    print(f'O resultado de {valor_1} * {valor_2} é {resultado}')
elif operacao == 'Subtração':
    resultado = int(valor_1) - int(valor_2) 
    print(f'O resultado de {valor_1} - {valor_2} é {resultado}')
elif operacao == 'Divisão':
    resultado = int(valor_1) / int(valor_2) 
    print(f'O resultado de {valor_1} / {valor_2} é {resultado}')
else: 
    print('Operação inválida. As operações possíveis são soma, multiplicação, subtração e divisão.')
