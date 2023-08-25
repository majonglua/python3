nome = 'kai'
altura = 1.80
massa = 67
imc = massa / (altura ** 2)

# Para formatar strings e habilitar o uso das fstrings, inserimos um 'f' no iní-
# cio da string, possibilitando usar variáveis dentro de uma string.

resultado_altura = f'{nome} tem {altura} metros de altura,'
resultado_massa_imc = f'massa de {massa} kilos e seu IMC é de {imc:.2f}.'
# O ':.xf' é uma forma de definir o número de casas decimais desejadas no resul-
# tado, onde 'x' é substituído pelo número de casas.

print(resultado_altura, resultado_massa_imc)
