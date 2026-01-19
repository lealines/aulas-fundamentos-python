class ContaBancaria:
    def __init__(self, nib, titular, saldo, limite):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_nib(self):
        return self.__nib

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_nib(self, novo_nib):
        self.__nib = novo_nib

    def set_titular(self, novo_titular):
        self.__titular = novo_titular

    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print('O saldo não pode ser negativo.')

    def set_limite(self, novo_limite):
            self.__limite = novo_limite
