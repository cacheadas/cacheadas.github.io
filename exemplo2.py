def calcular_area_e_perimetro(largura,altura):
    area=largura*altura
    perimetro=2*(largura+altura)
    return area,perimetro
resultado=calcular_area_e_perimetro(5,3)
print(resultado) #imprime (15,16)