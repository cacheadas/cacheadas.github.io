def calcular_area(largura, comprimento, unidade="m**2"):
    area=largura*comprimento
    print(f"a área é {area}{unidade}")
    
#chamaas da funcao:
calcular_area(10,5) #usando valoress parao
calcular_area(largura=3,comprimento=4,unidade="cm**2") #usando argumentos nomeados

