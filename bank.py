class BankAccount:
  def __init__(self, account_number, owner_name, initial_balance=0):
      self.account_number = account_number
      self.owner_name = owner_name
      self.balance = initial_balance

  def deposit(self, amount):
      if amount < 0:
          raise ValueError("Deposit amount must be positive")
      self.balance += amount

  def withdraw(self, amount):
      if amount < 0:
          raise ValueError("Withdrawal amount must be positive")
      if self.balance < amount:
          raise ValueError("Insufficient funds")
      self.balance -= amount

  def transfer(self, target_account, amount):
    try:
        self.withdraw(amount)
        target_account.deposit(amount)
    except Exception as e:
        print(f"Transfer failed: {e}")
        # Raise a new exception while maintaining the original context
        raise Exception("Transfer operation failed") from e


def handle_transactions():
  my_account = BankAccount(101, "Steve Rich", 500)
  friend_account = BankAccount(102, "Bessie Owens", 300)

  try:
      my_account.deposit(200)
      my_account.transfer(friend_account, 1500)  # This should fail
  except Exception as e:
      print(f"Operation failed: {e}")

  print(f"Account Balance (Steve Rich): £{my_account.balance}")
  print(f"Account Balance (Bessie Owens): £{friend_account.balance}")


handle_transactions()
