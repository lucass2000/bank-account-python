import unittest

from src.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.a = Account("João", 100)
        self.b = Account("Maria", 50)

    def test_deposit_and_withdraw(self):
        self.a.deposit(100)
        self.a.withdraw(40)
        self.assertEqual(self.a.balance, 160)

    def test_withdraw_exceeding_balance(self):
        with self.assertRaises(ValueError):
            self.a.withdraw(200)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.a.withdraw(-50)

    def test_transfer_between_accounts(self):
        self.a.transfer(self.b, 30)
        self.assertEqual(self.a.balance, 70)
        self.assertEqual(self.b.balance, 80)

    def test_sequence_of_operations(self):
        self.a.deposit(100)
        self.a.withdraw(50)
        self.a.transfer(self.b, 100)
        self.b.deposit(30)

        self.assertEqual(self.a.balance, 50)
        self.assertEqual(self.b.balance, 180)

    def test_invalid_initial_balance(self):
        with self.assertRaises(ValueError):
            Account("Carlos", -1)

    def test_empty_owner(self):
        with self.assertRaises(ValueError):
            Account("   ", 100)

    def test_transfer_to_same_account(self):
        with self.assertRaises(ValueError):
            self.a.transfer(self.a, 10)


if __name__ == "__main__":
    unittest.main()
