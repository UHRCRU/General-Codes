import uuid
import json
import re
from datetime import datetime
from abc import ABC, abstractmethod

# ==== Strategy Pattern Base ====
class PaymentResult:
    def __init__(self, success: bool, transaction_id: str, message: str):
        self.success = success
        self.transaction_id = transaction_id
        self.message = message
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> PaymentResult:
        pass

    @abstractmethod
    def get_method_name(self) -> str:
        pass

# ==== Concrete Strategies ====
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, expiry_date: str, cvv: str):
        if not re.match(r"^\d{16}$", card_number):
            raise ValueError("Invalid card number")
        if not re.match(r"^(0[1-9]|1[0-2])/\d{2}$", expiry_date):
            raise ValueError("Invalid expiry date format (MM/YY)")
        if not re.match(r"^\d{3}$", cvv):
            raise ValueError("Invalid CVV")

        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount: float) -> PaymentResult:
        print(f"💳 Charging ${amount:.2f} to card ending in {self.card_number[-4:]}")
        return PaymentResult(True, f"CC-{str(uuid.uuid4())[:8]}", "Credit Card payment successful")

    def get_method_name(self) -> str:
        return "Credit Card"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email):
            raise ValueError("Invalid email")
        self.email = email

    def pay(self, amount: float) -> PaymentResult:
        print(f"🅿️ Paying ${amount:.2f} via PayPal account {self.email}")
        return PaymentResult(True, f"PAYPAL-{str(uuid.uuid4())[:8]}", "PayPal payment completed")

    def get_method_name(self) -> str:
        return "PayPal"

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str, crypto_type: str):
        if not re.match(r"^[13a-zA-Z0-9]{26,35}$", wallet_address):
            raise ValueError("Invalid crypto wallet address")
        self.wallet_address = wallet_address
        self.crypto_type = crypto_type

    def pay(self, amount: float) -> PaymentResult:
        print(f"🪙 Sending {amount} {self.crypto_type} to wallet {self.wallet_address}")
        return PaymentResult(True, f"CRYPTO-{str(uuid.uuid4())[:8]}", "Crypto transfer successful")

    def get_method_name(self) -> str:
        return f"Crypto ({self.crypto_type})"

class ApplePayPayment(PaymentStrategy):
    def __init__(self, apple_id: str):
        if not re.match(r"^[\w\.-]+@apple\.com$", apple_id):
            raise ValueError("Invalid Apple ID")
        self.apple_id = apple_id

    def pay(self, amount: float) -> PaymentResult:
        print(f"🍎 Charging ${amount:.2f} using Apple Pay ID: {self.apple_id}")
        return PaymentResult(True, f"APPLE-{str(uuid.uuid4())[:8]}", "Apple Pay payment processed")

    def get_method_name(self) -> str:
        return "Apple Pay"

class BankTransferPayment(PaymentStrategy):
    def __init__(self, iban: str, bank_name: str):
        if not re.match(r"^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$", iban):
            raise ValueError("Invalid IBAN")
        self.iban = iban
        self.bank_name = bank_name

    def pay(self, amount: float) -> PaymentResult:
        print(f"🏦 Transferring ${amount:.2f} via {self.bank_name} (IBAN: {self.iban})")
        return PaymentResult(True, f"BANK-{str(uuid.uuid4())[:8]}", "Bank transfer successful")

    def get_method_name(self) -> str:
        return f"Bank Transfer ({self.bank_name})"

# ==== Transaction Logger ====
class TransactionLogger:
    def __init__(self, filename="transactions.json"):
        self.filename = filename

    def log(self, result: PaymentResult, method: str):
        entry = result.to_dict()
        entry['method'] = method

        try:
            with open(self.filename, "r+") as f:
                data = json.load(f)
                data.append(entry)
                f.seek(0)
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            with open(self.filename, "w") as f:
                json.dump([entry], f, indent=4)

# ==== CLI Interface ====
def get_payment_method() -> PaymentStrategy:
    methods = {
        "1": ("Credit Card", lambda: CreditCardPayment(
            input("Enter card number (16 digits): "),
            input("Enter expiry (MM/YY): "),
            input("Enter CVV (3 digits): ")
        )),
        "2": ("PayPal", lambda: PayPalPayment(
            input("Enter PayPal email: ")
        )),
        "3": ("Crypto", lambda: CryptoPayment(
            input("Enter wallet address: "),
            input("Enter crypto type (BTC/ETH/etc): ").upper()
        )),
        "4": ("Apple Pay", lambda: ApplePayPayment(
            input("Enter Apple ID (e.g., example@apple.com): ")
        )),
        "5": ("Bank Transfer", lambda: BankTransferPayment(
            input("Enter IBAN: "),
            input("Enter Bank Name: ")
        ))
    }

    print("\n💸 Select Payment Method:")
    for key, (name, _) in methods.items():
        print(f"{key}. {name}")

    while True:
        choice = input("Your choice (1-5): ")
        if choice in methods:
            try:
                return methods[choice][1]()
            except ValueError as e:
                print(f"⚠️  {e}, try again.")
        else:
            print("Invalid option, try again")

# ==== Main Payment Execution ====
def main():
    logger = TransactionLogger()
    print("\n💰 Welcome to the Payment System 💰")
    while True:
        try:
            amount = float(input("\nEnter amount to pay: "))
            strategy = get_payment_method()
            result = strategy.pay(amount)
            logger.log(result, strategy.get_method_name())
            print(f"✅ {result.message} (Transaction ID: {result.transaction_id})")
        except ValueError as e:
            print(f"⚠️  Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

        again = input("\nDo you want to make another payment? (y/n): ").lower()
        if again != 'y':
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
