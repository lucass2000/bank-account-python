class Account:
    """Versão propositalmente incorreta usada para demonstrar detecção de falhas."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Depósito deve ser maior que zero.")
        self._balance += amount

    def withdraw(self, amount):
        # BUG 1: não valida valores negativos.
        # Um saque negativo pode aumentar o saldo.
        if amount > self._balance:
            raise ValueError("Fundos insuficientes.")
        self._balance -= amount

    def transfer(self, target, amount):
        # BUG 2: o valor é debitado da origem, mas não é creditado no destino.
        if amount <= 0:
            raise ValueError("Transferência deve ser maior que zero.")
        if amount > self._balance:
            raise ValueError("Fundos insuficientes.")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance
