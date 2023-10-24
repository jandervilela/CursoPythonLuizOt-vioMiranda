frase = 'aaaooo'

i = 0
quantas_vezes_apareceu = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if quantas_vezes_apareceu < qtd_atual:
        quantas_vezes_apareceu = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{quantas_vezes_apareceu}x'
)