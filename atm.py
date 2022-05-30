class atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    
    def checkBalance(self):
        print("Your Balance is 50,000")
         
    def withdrawl(self,amount):
        print("You have withdrawn "+str(amount))
        new_amount=50000-amount
        print("Your remaining balance is "+str(new_amount))

def main():
    card_number=input("Insert your card number here:- ")
    pin_number=input("Insert your pin number here:- ")
        
    new_user=atm(card_number,pin_number)
    
    print("Choose your activity")    
    print("1.Balance Enquiry    2.Withdrawl ")
    activity=int(input("Enter the activity number :- "))

    if(activity == 1):
        new_user.checkBalance()
    elif(activity == 2):
        amount=int(input("Enter the amount to be withdrawn :- "))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number")

main()