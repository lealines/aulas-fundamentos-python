class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.limite = 400


    def levantar(self, valor):
        if valor > self.limite:
            print('Só pode levantar até 400€ por dia\n')
        else:
            print('Valor levantado com sucesso!\n')
            self.saldo -= valor


    def depositar(self, valor):
        self.saldo += valor
        print('Valor depositado com sucesso!\n')

    def consultar_saldo(self):
        print(f'Olá {self.titular}, o seu saldo é de {self.saldo:.2f}€\n')


nova_conta = Conta('Inês', 1000)

nova_conta.consultar_saldo()

nova_conta.levantar(50)

nova_conta.consultar_saldo()

nova_conta.depositar(50)

nova_conta.consultar_saldo()
