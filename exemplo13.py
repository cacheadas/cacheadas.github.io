def minha_funcao(**kwargs):
    for chave,valor in kwargs.items():
        print(f"{chave}:{valor}")
        
minha_funcao(nome="alice",idade=30,cidade="são paulo")