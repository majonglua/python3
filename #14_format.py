a = 'seleção'
b = '3'
c = 2.02300142843209

# Tudo em Python é um objeto, e objetos geralmente possuem métodos.
# Metódos são ações que podem ser feitas pelos objetos, como por exemplo, a fun-
# ção '.format()' incluída no final de um objeto.

formato = 'Flamengo = {Selecao}, Libertadores = {Titulos}, ano do penta = {CDB:.3f}'.format(
    Selecao=a, Titulos=b, CDB=c)

# 'a, b, c' são argumentos dentro da função format, também conhecidos como parâ-
# metros.

# Ao incluir a chave dentro da string, os valores da função.format' serão retor-
# nados por índice (0,1,2,etc).

# É possível nomear os parâmetros para maior facilidade de identificação, como
# 
print(formato)