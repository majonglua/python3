# Variáveis salvam algo na memória
# Por padrão escritas iniciando com letras minúsculas e separando-as com under-
# line, incluindo números se necessário, e utilizando '=' como sinal de atribui-
# ção.

# nome_da_variavel = expressão

seleção = 'Flamengo'
time = 'vasco da gama'

print(seleção, time, sep=' 4x0 ')

# Repetindo o código da aula #6 (aula6.py), podemos tornar o código mais limpo
# ao evitar sempre reescrever o mesmo argumento:

# print(int('4'), type(int('4')) se torna

val = int('4')

print(val, type(val))

# Para cumprir com boas práticas do Python, essa variável pode ser renomeada pa-
# ra algo mais descritivo

de_quanto_flamengo_ganhou = '4x0'

print('O Flamengo ganhou de', de_quanto_flamengo_ganhou)
