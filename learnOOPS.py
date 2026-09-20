class Account:
    def __init__(self, bal, acc_name):
        self.bal = bal
        self.acc_name = acc_name
    def debit(self, debit_amount):
        self.bal = self.bal - debit_amount
    def credit(self, credit_amount):
        self.bal = self.bal + credit_amount
    def check_bal(self):
        print(f"You're cuurent balance is : {self.bal}")


acc1 = Account(142000, 'KAULSON')


acc1.debit(121000)
acc1.credit(1000000000)
acc1.check_bal()