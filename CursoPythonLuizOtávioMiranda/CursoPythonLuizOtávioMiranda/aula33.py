"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 1000:
    contador += 2

    '''if contador == 6:
        print('Não vou mostrar o 6.')
        continue'''

    '''if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue'''

    print(contador)

    if contador == 1000:
        break


print('Acabou')