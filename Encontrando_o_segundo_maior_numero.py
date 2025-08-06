def secmaior(list):
    maior = max(list)
    segundo = min(list)
    for i in range(0, len(list)):
        if list[i] > segundo and list[i] < maior:
            segundo = list[i]
    return segundo


lista = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
print(secmaior(lista))