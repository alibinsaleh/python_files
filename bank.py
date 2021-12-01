import datetime
import os

class Account:
    def __init__(self, acc_num, acc_type, acc_owner, starting_balance=0.0, date_open=datetime.datetime.now()):
        self.acc_num = acc_num
        self.acc_type = acc_type
        self.acc_owner = acc_owner
        self.date_open = date_open
        self.starting_balance = starting_balance
        self.balance = starting_balance
        self.transactions = []

    def new_transaction(self, transaction):
        if transaction.trans_type.upper() == 'DEPOSIT':
            self.balance += transaction.trans_amount
        elif transaction.trans_type.upper() == 'WITHDRAW':
             self.balance -= transaction.trans_amount
   
        self.transactions.append(transaction)
    
    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def info(self):
        print('Account #:', self.acc_num)
        print('Name:', self.acc_owner)
        print('Starting Balance:', self.starting_balance)
        print('Date Open:', self.date_open.date())
        print('Balance:', self.balance)


    def show_transactions(self):
        print('\u250f'.ljust(98, '-')+'\u2513')
        print('| '+'Transaction #'.ljust(14, ' ')+'| '+'Trans. Type'.ljust(12, ' ')+'| '+'Trans. Desc.'.ljust(50, ' ')+'| '+'Trans. Amount'.ljust(13, ' ')+' |')
        print('|'.ljust(16, '-')+'|'.ljust(14, '-')+'|'.ljust(52, '-')+'|'.ljust(15, '-')+' |')
        for t in self.transactions:
            print('| '+str(t.trans_id).ljust(14, ' ')+'| '+t.trans_type.ljust(12, ' ')+'| '+t.trans_desc.ljust(50, ' ')+'| '+str(t.trans_amount).ljust(13, ' ')+' |')
            #print(t.trans_id, t.trans_type, t.trans_desc, t.trans_amount)
            print('\u2517'.ljust(16, '-')+'+'.ljust(14, '-')+'+'.ljust(52, '-')+'+'.ljust(16, '-')+'\u251B')
    
   
class Transaction:
    def __init__(self, trans_id, acc_num, trans_type, trans_desc, trans_amount=0.0):
        self.trans_id = trans_id
        self.acc_num = acc_num
        self.trans_type = trans_type
        self.trans_desc = trans_desc
        self.trans_amount = trans_amount

if __name__ == "__main__":
    
    os.system('clear')

    ali = Account('10001', 'Current', 'Ali Almohammed Saleh')
    ali.new_transaction(Transaction(1, '10001', 'Deposit', 'Salary', 19054))
    ali.new_transaction(Transaction(2, '10001', 'Withdraw', 'ATM withdraw', 1500))
    ali.new_transaction(Transaction(3, '10001', 'Withdraw', 'Alyahya Supermarket', 400))
    ali.new_transaction(Transaction(4, '10001', 'Withdraw', 'Jarrir Bookstore', 200))
    
    ali.info()
    ali.show_transactions()

