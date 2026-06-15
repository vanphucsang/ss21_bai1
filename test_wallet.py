import unittest
from wallet import deposit
from wallet import transfer

class TestWallet(unittest.TestCase):
    def test_deposit_success(self):
        result = deposit(0, 100000)
        self.assertEqual(
            result,
            100000
        )
    def test_transfer_insufficient_balance(self):
        with self.assertRaises(ValueError):
            transfer(
                100000,
                "0987654321",
                200000
            )
    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            deposit(
                0,
                -1000
            )
if __name__ == "__main__":
    unittest.main()