import unittest

from src.account_buggy import Account


class TestBuggyAccount(unittest.TestCase):
    """Os testes abaixo são esperados a falhar na versão propositalmente bugada."""

    def setUp(self):
        self.a = Account("João", 100)
        self.b = Account("Maria", 50)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.a.withdraw(-50)

    def test_transfer_between_accounts(self):
        self.a.transfer(self.b, 30)
        self.assertEqual(self.a.balance, 70)
        self.assertEqual(self.b.balance, 80)


if __name__ == "__main__":
    unittest.main()
