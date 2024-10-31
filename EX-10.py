# Criando uma lista inicial
fila = ["pombo", "lagartixa", "calango"]

# Com append adicionamos um quarto item por exemplo sempre ao final
fila.append("cachorro")
#usando pop nós retiramos o primeiro item que entrou em nossa lista ou já estava em nossa lista
Primeiro = fila.pop(0)
# traduzindo é o primeiro a entrar e primeiro a sair, igual fila de caixa
print("Lista após adicionar e remover pelo FIFO:", fila)
print("Primeiro item removido:", Primeiro)