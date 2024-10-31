lista = ["alegria", "ansiedade", "sono", "fome", "preguiça", "coxinha"]
indice = 3 # aqui essa variavel controla nosso belo indice.

# While que segue enquanto o indice é menor que 5
while indice <= 5:
    print(lista[indice]) # faz o print do indice que estamos até o fim da lista, mas sempre um por vez
    indice += 1  # adicionamos um valor a mais no indice para ele conseguir printar o proximo item

'''
nós poderiamso usar o While true, mas para oque fariamos um loop infinito com necessidade de colocar um break para 
para se posso fazer apenas um loop até o indice 5, seria mais verboso.
Se a gente usa-se mais indices ai sim seria interessante usar o While true ou for.
'''