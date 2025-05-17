class ATM:
  def __init__(self):
    self.balance = 5000
    self.pin = "1234"

  def check_pin(self, input_pin):
    return input_pin == self.pin

  def check_balance(self):
    return f"Your current balance is Rs: {self.balance}"

  
  def deposit(self, amount, input_pin):
    if not self.check_pin(input_pin):
      return "Invalid PIN"
    if amount <= 0:
      return "Deposit amount must be greater than zero."
    self.balance += amount
    return f"Rs: {amount} deposited successfully. New balance: Rs {self.balance}"

  def withdraw(self, amount, input_pin):
    if not self.check_pin(input_pin):
      return "Invalid PIN"
    if amount <= 0:
      return "withdrawl amount must be greater than zero."
    if amount > self.balance:
      return "Insufficient balance"
    self.balance -= amount
    return f"Rs: {amount} withdrawn successfully. Remaining balance: Rs {self.balance}"

  def exit(self):
    return "Thank you for using the ATM, Goodbye!"


atm = ATM()

print(atm.check_balance())         # ✅ Should return the current balance
print(atm.deposit(500, "1234"))          # ✅ Deposit ₹500
print(atm.withdraw(300, "1234"))         # ✅ Withdraw ₹300
print(atm.check_balance())         # ❌ Wrong PIN
print(atm.withdraw(6000, "1234"))        # ❌ Exceeds balance
print(exit)


