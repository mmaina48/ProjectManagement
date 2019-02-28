class Card:
    balance=0   #property

    def __init__(self,bal):
        self.balance=bal

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -= amount
            return self.printreceit(self.balance,amount)
        else:
            return "zerro "

    def printreceit(self,balance,withdraw):
        return """  Amount : ....{}
                    Balance..""".format(withdraw,balance)






