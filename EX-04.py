lista = ["   joao   ", "   maria   ", "  joana  "] # nossa bela lista
nova_lista = [nome.strip() for nome in lista] # Strip é O METODO para tirarmos espaço em branco
print(nova_lista)
'''
basicamente fiz um metodo que percorre nossa lista, item por item e com o strip ele remove as partes em branco.
Dava para usar split tambem mas teriamos de criar uma nova lista para inserir os itens sem espaço, oque deixa o 
código maior e nós não queremos isso...
'''