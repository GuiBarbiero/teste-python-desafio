response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

produtosCaros = []  # Lista que usei para guardar os valores
# loop para percorrermos todo o json
for lojas in response:
    # Filtra os produtos que têm preço maior que 30
    Filtrados = [produto for produto in lojas["produtos"] if produto["preço"] > 30]
    # Nesta parte ele olha se temos no json produtos com valor maior que 30
    if Filtrados:
        produtosCaros.append({
            "nomeLoja": lojas["nome"],  #adiciona na lista o nome da loja e o produto no caso id,nome e preço
            "produtos": Filtrados  # parte dos produtos que filtramos
        })
import json
print(json.dumps(produtosCaros, indent=4, ensure_ascii=False))
#PORQUE FIZ ASSIM?
'''Usei list comprehendion tanto pela facilidade, pois uso em meu dia a dia e por 
    questoões de verbosidade, usar um for ou while diminui a necessidade de criar
    mais lógicas para realizar a filtragem, sem contar que caso a gente use um json
    com milhares de lojas e etc, a velocidade e eficiencia usando outros metodos iria 
    aumentar, causando assim um atraso em produção. asadadsadasds
'''




