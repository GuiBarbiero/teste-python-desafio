lista = [5,8,3,0,8,1,9,10,20,30]
lista.sort() # nosso lindo e belo sort() ele basicamente faz todo o trabalho de ordenar a lista so que in-place
print(lista)

'''
O in-place ele basicamente quer dizer que a lista original é alterada, no caso inves de criarmos uma nova e ele verificar
termo por termo e ir ordenado, algo como o bouble sorte, aqui ele só reescreve a original, poupando código e tempo.

Ta e porque não usamos sorte?
Se compararmos a efeiciencia entre eles, o sort ganha em disparada em questão de tempo e velocidade.
Até em verbosidade o sort ganha, o bouble pode ser simples e sem complexidade para trica rapida de elementos ordenando
eles.

para entender todos os metodos oque recomendo é ver este video usando ordenação visualizada, caso seja leito e queria ver mais
https://www.youtube.com/watch?v=rQTQF46o16k&ab_channel=GurudaCi%C3%AAncia
'''