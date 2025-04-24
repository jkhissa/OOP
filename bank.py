class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

# Public Getter Methods
    # These methods are public and can be accessed from outside the class
    # They provide access to the private attributes of the class
    # They are used to retrieve the values of the private attributes
    # They do not modify the state of the object
    # They are used to provide a controlled way to access the private attributes
    # They are used to encapsulate the private attributes
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance -= amount
