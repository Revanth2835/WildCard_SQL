class BankAccount:
    def __init__(self, owner, balance):
        # Public attribute — can be accessed freely
        self.owner = owner
        
        # Protected attribute — conventionally for internal or subclass use
        self._account_type = 'Savings'
        
        # Private attribute — name mangled to prevent direct external access
        self.__balance = balance

    # Public method to display account details
    def display_info(self):
        print(f"Owner: {self.owner}")
        print(f"Account Type: {self._account_type}")
        # Accessing the private attribute safely within the class
        print(f"Balance: ₹{self.__balance}")

    # Getter method for the private variable __balance
    def get_balance(self):
        return self.__balance

    # Setter method for the private variable __balance
    def set_balance(self, amount):
        # Only allow valid updates through controlled conditions
        if amount < 0:
            print("Error: Balance cannot be negative.")
        else:
            self.__balance = amount
            print(f"Balance updated to ₹{self.__balance}")

# --- Example Usage ---

# Create an instance of BankAccount
account = BankAccount("Alice", 5000)

# Accessing public variable directly
print(account.owner)  # Works fine

# Accessing protected variable (possible but discouraged)
print(account._account_type)

# Accessing private variable directly will raise AttributeError
# print(account.__balance)  # ❌ AttributeError

# Using getter to safely access private data
print("Initial balance:", account.get_balance())

# Using setter to safely modify data
account.set_balance(6000)  # ✅ Valid update
account.set_balance(-500)  # ❌ Invalid update prevented

# Display full information
account.display_info()
