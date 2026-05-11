#USANDO FOR
def mostra_palavra_for(palavra):
    #para cada indic desse intervalo
    for i in range(len(palavra)):
        print(i, palavra[:len(palavra) -i])

#USANDO RECURSAO
def mostra_palavra_rec(palavra):
    if len(palavra) == 0:
        return
    print('antes da chamda', palavra)
    mostra_palavra_rec(palavra[:-1])
    print('depois da chamda', palavra)
    return

def fibonacci(n):
    if n ==0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

mostra_palavra_rec('ola')
print(fibonacci(10))