class Account:
    """Representa uma conta bancária simples para fins acadêmicos."""

    def __init__(self, owner: str, balance: float = 0.0):
        if not owner or not owner.strip():
            raise ValueError("O titular da conta não pode ser vazio.")
        if balance < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")

        self.owner = owner.strip()
        self._balance = float(balance)

    def deposit(self, amount: float) -> None:
        """Deposita um valor positivo na conta."""
        if amount <= 0:
            raise ValueError("O depósito deve ser maior que zero.")

        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Realiza um saque, desde que o valor seja válido e haja saldo."""
        if amount <= 0:
            raise ValueError("O valor de saque deve ser maior que zero.")
        if amount > self._balance:
            raise ValueError("Fundos insuficientes.")

        self._balance -= amount

    def transfer(self, target: "Account", amount: float) -> None:
        """Transfere um valor desta conta para outra conta."""
        if not isinstance(target, Account):
            raise TypeError("A conta de destino deve ser uma instância de Account.")
        if target is self:
            raise ValueError("A conta de destino deve ser diferente da conta de origem.")
        if amount <= 0:
            raise ValueError("A transferência deve ser maior que zero.")
        if amount > self._balance:
            raise ValueError("Fundos insuficientes.")

        self._balance -= amount
        target._balance += amount

    @property
    def balance(self) -> float:
        """Retorna o saldo atual da conta."""
        return self._balance

    def __repr__(self) -> str:
        return f"Account(owner={self.owner!r}, balance={self._balance:.2f})"
