myCustomerlist = []
myCardlist = []
class Customer:
    def __init__(self):
        self.id = None
        self.name = None
class Customer:
    def __init__(self):
        self.id = None
        self.name = None
        self.acc_num = None
        self.balance = None
        self.credit_cards = []
    def create_new_customer(self):
        self.id = input("Enter Customer ID: ")
        self.name = input("Enter Customer Name: ")
        self.acc_num = input("Enter Customer Account Number: ")
        self.balance = input("Enter Customer Balance: ")
    def transfer_funds(self,bene_customer, amount):
        self.balance -= amount
        bene_customer.balance += amount
    def card_link(self, card):
        self.credit_cards.append(card)
    def display_customer_details(self):
        print(self.id)
        print(self.name)
        print(self.acc_num)
        print(self.balance)
        print(self.credit_cards)
class Card:
    def __init__(self):
        self.card_num = None
        self.cvv = None
        self.expiry_date = None
        self.balance = None
    def create_new_card(self):
        self.card_num = input("Enter Card Number: ")
        self.cvv = input("Enter CVV: ")
        self.expiry_date = input("Enter Expiry Date: ")
        self.balance = input("Enter Balance: ")
    def display_card_details(self):
        print(self.card_num)
        print(self.cvv)
        print(self.expiry_date)
        print(self.balance)
print("1. Create new Customer")
print("2. Create new Card")
print("3. Transfer funds")
print("4. Card link")
print("5. Display Customer Details & Card Details")
print("6. Exit")
customer = Customer()
card = Card()
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer.create_new_customer()
        myCustomerlist.append(customer)
    if choice == 2:
        card.create_new_card()
        myCardlist.append(card)
    if choice == 3:
        myCustomerlist[0].transfer_funds(myCustomerlist[1], 200)
        print(myCustomerlist[0].display_customer_details())
        print(myCustomerlist[1].display_card_details())
    if choice == 4:
        customer.card_link(card)
    if choice == 5:
        customer.display_customer_details()
        card.display_card_details()
    if choice == 6:
        exit()


