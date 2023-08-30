# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

while True:
    login_nome = input('Insira seu login: ')
    versao_baixar = input(
        'Insira  a versão que deseja baixar, '
        '(1) para versão 4.2 e (2) para versão 4.3: ')
    versao_4_2 = 'https://www.youtube.com/watch?v=zObCCCsCo2I'
    download_4_2 = '%s, baixe a versão 4.2 em %s.' % (login_nome, versao_4_2)
    versao_4_3 = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    download_4_3 = '%s, baixe a versão 4.3 em %s.' % (login_nome, versao_4_3)

    if versao_baixar == '1':
        print(download_4_2)
        break
    elif versao_baixar == '2':
        print(download_4_3)
        break
    else:
        print('Versão inválida.')
        continue