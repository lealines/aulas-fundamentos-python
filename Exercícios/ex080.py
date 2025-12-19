def analisar_notas(notas):

    if not notas:
        return {"erro": "Nenhuma nota fornecida"}

    quantidade = len(notas)
    maior_nota = max(notas)
    media = sum(notas) / quantidade

    if media > 12:
        situacao = "boa"
    elif media < 9.5:
        situacao = "fraca"
    else:
        situacao = "razoável"

    resultado = {
        "Quantidade": quantidade,
        "Maior nota": maior_nota,
        "Média": media,
        "Situação": situacao
    }

    return resultado

notas_turma = []

while True:
    entrada = input("Digite a nota do aluno ('stop' para parar): ")
    if entrada.lower() == "stop":
        break
    try:
        nota = float(entrada)
        if nota < 0 or nota > 20:
            print("\nValor inválido! Insira um valor entre 0 e 20.")
        else:
            notas_turma.append(nota)
    except ValueError:
        print("Valor inválido! Digite um número.")

resultado = analisar_notas(notas_turma)
print("\n--- Resultado da turma ---\n")
for chave, valor in resultado.items():
    print(f"{chave.title()}: {valor}")