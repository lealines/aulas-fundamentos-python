class ContaBancaria:
    def __init__(self, nib: int, titular, saldo, limite):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def nib(self):
        return self.__nib

    @nib.setter
    def nib(self, valor):
        self.__nib = valor

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print('O saldo não pode ser negativo.')

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        if valor >= 0:
            self.__limite = valor
        else:
            print('O limite não pode ser negativo.')

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print('\nValor depositado com sucesso!')
        else:
            print('O valor do depósito deve ser positivo.')

    def levantar(self, valor):
        if 0 < valor <= self.saldo and valor <= self.limite:
            self.saldo = self.saldo - valor
            print('\nValor levantado com sucesso!')
        else:
            print('Levantamento não permitido. Verifique o saldo e limite.')

conta = ContaBancaria(5012345655 , 'Inês Leal', 1000, 400)

print('NIB:', conta.nib)
print('Titular:', conta.titular)
print('Saldo:', conta.saldo)
print('Limite:', conta.limite)

conta.depositar(200)
print('Após depósito:')
print('Saldo:', conta.saldo)

conta.levantar(300)
print('Após levantamento:')
print('Saldo:', conta.saldo)