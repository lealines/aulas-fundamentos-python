def cabecalho(txt):
    largura = len(txt)
    tracos = '=' * (largura * 2)

print(tracos)
print(f'{txt:^{largura}}')
print(tracos)

cabecalho(input('Digite uma mensagem: '))