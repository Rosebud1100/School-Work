myCustomerlist = []
myCardlist = []
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
        self.balance = float(input("Enter Customer Balance: "))
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
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer = Customer()
        customer.create_new_customer()
        myCustomerlist.append(customer)
    elif choice == 2:
        card = Card()
        card.create_new_card()
        myCardlist.append(card)
    elif choice == 3:
        sender_index = int(input("Enter sender customer index: "))
        receiver_index = int(input("Enter receiver customer index: "))
        amount = float(input("Enter amount to transfer: "))

        myCustomerlist[sender_index].transfer_funds(myCustomerlist[receiver_index], amount)
        myCustomerlist[sender_index].display_customer_details()
        myCustomerlist[receiver_index].display_customer_details()
    elif choice == 4:
        if choice == 4:
            cust_index = int(input("Enter customer index: "))
            card_index = int(input("Enter card index: "))

            myCustomerlist[cust_index].card_link(myCardlist[card_index])
    elif choice == 5:
        cust_index = int(input("Enter customer index: "))
        card_index = int(input("Enter card index: "))
        myCustomerlist[cust_index].display_customer_details()
        myCardlist[card_index].display_card_details()
    else:
        exit()
