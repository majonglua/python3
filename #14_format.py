a = 'seleção'
b = '3'
c = 2.02300142843209

# Tudo em Python é um objeto, e objetos geralmente possuem métodos.
# Metódos são ações que podem ser feitas pelos objetos, como por exemplo, a fun-
# ção '.format()' incluída no final de um objeto.

formato = 'Flamengo = {}, Libertadores = {}, ano do penta = {:.3f}'.format(a, b, c)

# 'a, b, c' são argumentos dentro da função format, também conhecidos como parâ-
# metros.

# Ao incluir a chave dentro da string, os valores da função.format' serão retor-
# nados em ordem.

print(formato)