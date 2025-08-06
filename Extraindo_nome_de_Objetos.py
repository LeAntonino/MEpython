
def nomeextract(object):
    listanomes = []
    for i in object:
        listanomes.append(i['nome'])
    return listanomes


objeto = [
    {'nome': 'Antonino','sexo': 'masculino', 'id': 1}, 
    {'nome': 'Julia','sexo': 'feminino', 'id': 2}, 
    {'nome': 'Davi','sexo': 'masculino', 'id': 3}, 
    {'nome': 'Eduarda','sexo': 'feminino', 'id': 4}
    ]
print(nomeextract(objeto))