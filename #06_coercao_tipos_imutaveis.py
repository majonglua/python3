# O Python só pode concatenar str com str, por exemplo:
# print('1' + 1) # TypeError: can only concatenate str (not "int") to str
# print('1' + '1') # Concatena as duas strings corretamente, resultando em 11

print('1' + '1')

# Esta é uma propriedade dos tipos imutáveis/primitivos (str, int, float, bool)

# Caso necessário realizar a coerção de um tipo, se utiliza uma função (classe)
# para especificar o tipo final, por exemplo:

print(int('4'), type(int('4')))

print(int('4') + 4)

print(float('4') + 4)

print(bool(4 == 4.00001))

print(str(bool('4')))
