def cabecalho(msg):
    size = (len(msg))
    print("-="*(size*2))
    print(f"{msg:^{size*4}}")
    print("-="*(size*2))


cabecalho(input("Insere uma mensagem: "))