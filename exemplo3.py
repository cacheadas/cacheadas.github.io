def calcular_media(numeros):
    soma=sum(numeros)
    quantidade=len(numeros)
    media=soma/quantidade
    return media
notas=[8,7,9,10]
media_final=calcular_media(notas)
print(f"a media e:{media_final}")