def encontra(list, value):
    encontrado = False
    for i in range(0, len(list)):
        if list[i] == value:
            encontrado = True
    return encontrado


lista = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
print(encontra(lista, 1))
print(encontra(lista, 0))