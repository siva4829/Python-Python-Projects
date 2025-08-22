import time as tm
class Auction:
    
    def __init__(self):
        self.head=[]
        
    def bet_amount(self,amount):
        if not self.head:
            self.head.append(amount)
            
        elif amount not in self.head and amount>self.head[-1]:
             self.head.append(amount)
             self.head.sort(reverse=True)
             
        else:
            print("Already that bet is exist")     
        
    def highest_bid(self):
        if not self.head:
            print("No amount is added")
            return
            
        else:
                
          return  self.head[0]
        
if __name__=="__main__":
    cust=Auction() 
    while True:
          tm.sleep(0.5)
          print("\n----Welcome to Auction House ----\n")
          print("1.Bet amount")
          print("2.show highest bid")
          print("3.exit")
          try:
              choice=int(input("Enter your choice:"))
          except ValueError:
              print("Enter integer value")
                  
          if choice == 1:
              try:
                  amount=int(input("Place your amount :"))
                  cust.bet_amount(amount)
              except ValueError:
                  print("Enter integer value")  
                  
          elif choice == 2:
              print(cust.highest_bid())  
              
          elif  choice == 3 :
              print("Exiting the program....")
              tm.sleep(1)
              exit(0)
           
          else:
              print("Enter valid input")              
