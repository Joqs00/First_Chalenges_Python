class conta_bancaria():
    def __init__(self, titular= '', saldo= 0, ativo= False):
        self._titular = titular.title()
        self._saldo =  float(saldo)
        self._ativo = ativo

    def __str__(self):
        return f'\n Titular da conta:  {self._titular}\n Saldo: R${self._saldo}\n Ativo: {'Sim' if self._ativo else 'Não'}'
    
    @classmethod
    def ativar_conta(cls, conta):
        if not conta._ativo:
            conta._ativo = True
            print(f'\nA conta de {conta._titular} foi ativada.\n')
        else:
            print(f'\nA conta de {conta._titular} já está ativada.\n')



Karla = conta_bancaria('Karla', '1000')


print(Karla)

conta_bancaria.ativar_conta(Karla)

print(Karla)

Shuu = conta_bancaria('Shuu', 256,30)

print(f'\n{Shuu._titular}\n')

class ClienteBanco():
    def __init__(self, nome='', saldo= 0,  divida= 0, credito= 0, ativo= False):
        self.nome = nome.title()
        self.saldo = float(saldo)
        self.divida = float(divida)
        self.credito = float(credito)
        self.ativo = ativo

    @classmethod
    def calculo_credito(cls, conta):
        if conta.divida == 0:
            conta.credito = 1000
        elif conta.divida >=1 and conta.divida <= 200 :
            conta.credito = 500
        else:
            conta.credito = 0

    def __str__(self):
        return f'Titular: {self.nome}\nSaldo: R${self.saldo}\nDívida: R${self.divida}\nCrédito: R${self.credito}\n \n'

Kynn = ClienteBanco('Kynn', 200, 0)
Bend = ClienteBanco('Bend', -500, 300)
Guaxo = ClienteBanco('Guaxo', 100, 150)

ClienteBanco.calculo_credito(Kynn)
ClienteBanco.calculo_credito(Bend)
ClienteBanco.calculo_credito(Guaxo)

print(Kynn,Guaxo,Bend)