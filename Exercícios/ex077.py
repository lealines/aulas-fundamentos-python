from datetime import datetime

def carta(ano_nascimento, ficheiro='resultado.txt'):

    ano_atual = datetime.now().year

    idade = ano_atual - ano_nascimento

    if idade >= 18:

        txt = f'{idade} anos, pode tirar a carta de condução.'
    elif idade < 16:

        txt = f'{idade} anos, não pode tirar a carta de condução.'
    else:

        txt = f'{idade} anos, pode tirar com autorização do encarregado de educação.'

    with open(ficheiro, 'w', encoding='utf-8', errors='ignore') as file:

        file.write(txt)

    print("\nInformação gravada no ficheiro:", ficheiro)

ano = int(input("Insere o ano de nascimento: "))

carta(ano)