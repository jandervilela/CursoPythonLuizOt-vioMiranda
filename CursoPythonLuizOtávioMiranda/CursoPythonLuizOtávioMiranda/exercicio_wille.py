'''
Iterando strings com wille
'''

#.......012345678910
nome = 'Jander Vilela' # Iteraveis
#......1110987654321
tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)