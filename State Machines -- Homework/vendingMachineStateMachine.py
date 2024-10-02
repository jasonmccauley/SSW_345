class SM():
    def __init__(self):
        self.state = "waiting" 
        print(self.state)
        self.money_entered = 0

    def insert_dollar(self):
        self.money_entered += 1.00
        self.state = "collecting"
        print(self.state)
        print(f"Dollar accepted, you have entered ${round(self.money_entered, 2)}")
        if(self.money_entered >= 0.75):
            self.buy_drink() 

    def insert_quarter(self):
        self.money_entered += 0.25
        self.state = "collecting"
        print(self.state)
        print(f"Quarter accepted, you have entered ${round(self.money_entered, 2)}")
        if(self.money_entered >= 0.75):
            self.buy_drink()

    def insert_dime(self):
        self.money_entered += 0.10
        self.state = "collecting"
        print(self.state)
        print(f"Dime accepted, you have entered ${round(self.money_entered, 2)}")
        if(self.money_entered >= 0.75):
            self.buy_drink()

    def insert_nickel(self):
        self.money_entered += 0.05
        self.state = "collecting"
        print(self.state)
        print(f"Nickel accepted, you have entered ${round(self.money_entered, 2)}")
        if(self.money_entered >= 0.75):
            self.buy_drink()

    def cancel_sale(self):
        self.state = "cancelling"
        print(self.state)
        print(f"You have been refunded ${round(self.money_entered, 2)}")
        self.money_entered -= self.money_entered
        self.state = "waiting"
        print(self.state)

    def buy_drink(self):
        self.state = "buying"
        print(self.state)
        print(f"You have purchased a drink")
        self.money_entered -= 0.75
        if(self.money_entered > 0):
            print(f"You have been refunded the extra ${round(self.money_entered, 2)}")
            self.money_entered -= self.money_entered
        self.state = "waiting"
        print(self.state)
        
print("Scenario 1--")
vending_machine1 = SM()
vending_machine1.insert_quarter()
vending_machine1.insert_quarter()
vending_machine1.insert_quarter()
print("")

print("Scenario 2--")
vending_machine2 = SM()
vending_machine2.insert_quarter()
vending_machine2.cancel_sale()
print("")

print("Scenario 3--")
vending_machine3 = SM()
vending_machine3.insert_dime()
vending_machine3.insert_dollar()
print("")