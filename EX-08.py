import requests
def contadora(): # função para ficar mais compreensivel e lógico
    # Aqui estamos realizando a requisição
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    #Aqui convertemos para Json nossa requisição para facilitar
    todos = response.json()
    #Variaveis que estou usando para guardar a quantidade das tarefas.
    completadas = 0
    pendentes = 0

    # Aqui estou somando um valor a mais a cada tarefa que ele ve pendente ou completa na variavel acima que criei
    for tarefas in todos:
        if tarefas['completed']:
            completadas += 1
        else:
            pendentes += 1
    # Retorna a formatação bonita
    return f"Tarefas completadas: {completadas} | Tarefas pendentes: {pendentes}"

# Chama a função e imprime o resultado formatado de forma mais bonita :)
resultado = contadora()
print(resultado)
'''
Não conheço outro metodo de fazer alem desse. Para alterar um pouco o código daria para concatenar a saida das tarefas
mas seria menos compreensivel que usar Fstring.
'''