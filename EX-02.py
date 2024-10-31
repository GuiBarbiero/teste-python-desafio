responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

precoB = None
for produto in responsejson["produtos"]: # Loop para percorrer nossa lista
    if produto["nome"] == "Produto B": # aqui ele procura se o nosso nome de produto é produto B, caso seja ele faz a ação de pegar o preço
        precoB = produto["preço"]
        break  #para o código quando encontra o valor B
print(f"O preço do Produto B é: {precoB}")

'''
De forma simples e lógica semelhante ao outro poderiamos ter usado while, ambos dão certo
Neste caso.

Poderiamos ter usado apenas 5 linhas usando a função next porem seria mais complexo e de menor entendimento caso outra pessoa
vá visualizar seu código, portanto caso a gente tenha uma lista maior, com mais dados seria uma possibilidade usar next()

Algo como next((produto for produto in responsejson["produtos"] if produto["nome"] == "Produto B"), None)

Nisto nós basicamente colocamos a linha de verificação de nome na mesma linha diminuindo.
Seria interessante usar next tambem se você quer um resultado mais rapido e menos verbosidade em um código que você fez.
'''