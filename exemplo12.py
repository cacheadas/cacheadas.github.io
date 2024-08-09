def calcular_media(*numeros):
    soma=sum(numeros)
    quantidade=len(numeros)
    media=soma/quantidade
    return media

#chamada da funcao:
notas=[8,7,9,10]
media=calcular_media(*notas) #desempacotando a lista
print(f"a média é {media}")