# 'if', 'elif' e 'else' representam 'se, 'se não se' e se não'. Eles abrem di-
# versas possibilidades no  fluxo do código, como podemos aplicar no código da
# aula anterior.

valor_1 = input('Digite o primeiro valor: ')
valor_2 = input('Digite o segundo valor: ')
operacao = input('Digite qual será a operação: ')
soma = float(valor_1) + float(valor_2)
mult = float(valor_1) * float(valor_2) 
div = float(valor_1) / float(valor_2)
sub = float(valor_1) - float(valor_2)

if operacao == 'Soma':
    print(f'O resultado de {valor_1} + {valor_2} é {soma}')
elif operacao == 'Multiplicação':
    print(f'O resultado de {valor_1} * {valor_2} é {mult}')
elif operacao == 'Subtração':
    print(f'O resultado de {valor_1} - {valor_2} é {sub}')
elif operacao == 'Divisão':
    print(f'O resultado de {valor_1} / {valor_2} é {div}')
else: 
    print('Operação inválida. As operações possíveis são soma, multiplicação, subtração e divisão.')
