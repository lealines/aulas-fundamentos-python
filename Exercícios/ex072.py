from time import sleep

def contagem(inicio:int, fim:int, passo:int):
    for c in range(0, 21, 2):
        print(f"{c}")
        sleep(0.5)
    print("="*10)
    for j in range(10, 0, -1):
        print(f"{j}")
        sleep(0.5)
    print("=" * 10)
    fim2 = fim+1
    for k in range(inicio, fim2, passo):
        print(f"{k}")
        sleep(0.5)

contagem(int(input("Insere um inicio: ")),int(input("Insere um fim: ")), int(input("Insere um passo: ")))