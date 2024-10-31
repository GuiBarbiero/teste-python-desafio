import requests

def dadosPessoas():
    # Linda e bela requisição, explicada no outro exercicio tambem.
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    # Converte para Json o formato
    usuarios = response.json()
    # Nossa lista para armazenar oque desejamos
    Filtrados = []
    # loop para coletarmos os dados um por um de cada usuario
    for usuario in usuarios:
        nome = usuario['name']
        username = usuario['username']
        email = usuario['email']
        rua = usuario['address']['street']
        numero = usuario['address']['suite']
        # Aqui estou usando append para adicionarmos oque coletamos da api, no caso nome user e etc na nossa lista
        Filtrados.append({
            "nome": nome,
            "username": username,
            "email": email,
            "rua": rua,
            "numero": numero
        })
    # retorna a lista filtrada para utilizarmos
    return Filtrados
# Chamamos a função aqui falando que nosso resultado é igual a dadosPessoas
resultado = dadosPessoas()
# Percorre resultado e inseri em item o valor de cada usuario
for item in resultado:
    print(item)
