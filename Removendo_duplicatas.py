def duplicado(list):
    listanova = []
    for i in range(0,len(list)):
        if list[i] not in listanova:
            listanova.append(list[i])
    return listanova


lista = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
print(duplicado(lista))