lista = ["joao", "ana", "joana", "joao", "ricardo", "joao"]
# Aqui ele substitui o joao por maria verificando o nome na lista (sem segredo)
lista = ["maria" if nome == "joao" else nome for nome in lista]
print(lista)

'''
Podemos usar um for? Podemos mas você teria que usar range, len seria mais verboso. Claro se tivesse mais conteudo seria
mais interessante usar For para questões de entendimento de código, sem contar que ele altera na lista original.
'''