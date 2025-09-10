import random,time,os


class Bingo:
  
  def __init__(self):
      self.Table = [['•' for j in range(5)] for i in range(5)]
      
  def display(self):
    size = 5
    border = "+-----" * size + "+"
    print(border)
    for row in self.Table:  
        print("|" + "|".join(f"{cell:^5}" for cell in row) + "|")
        print(border)
              
  def get_user_sequence(self):
      try :
          used_number=set()
          for i in range(5):
              for j in range(5):
                 temp=int(input(f"Enter{i}{j} (1-25) : "))
                 if temp <=0 or temp>25:
                    while temp <=0 or temp>25:
                        temp=int(input(f"Enter{i}{j} (1-25) : "))
                    used_number.add(temp)
                    self.Table[i][j]=temp    
                 else:
                    while temp:
                        if temp not in used_number:
                            used_number.add(temp)
                            self.Table[i][j]=temp
                            break
                        else:
                            temp=int(input(f"Enter{i}{j} (1-5) : "))
                 self.display()
                 time.sleep(2)
          os.system('clear')              
          self.check_winner()              
      except typeError:
       print("Enter valid type data")
      except Exception as e:
       print(e)   
       
       
  def game(self,number):
       self.check=set()
       if number not in self.check:
           for i,ind in enumerate(self.Table):
               if number in ind:
                  inde=ind.index(number)
                  self.check.add(number)
                  r,c=i,inde
                  self.Table[r][c]="*"
                  self.check_winner()
       else:
           print("The number is already removed")
           x=int(input("Enter not used number"))
           self.game(x)
           
              
  def check_winner(self):
    if not hasattr(self, "completed_lines"):
        self.completed_lines = set()  # keep track of which lines are already complete

    # Check rows
    for i in range(5):
        if all(self.Table[i][j] == "*" for j in range(5)):
            self.completed_lines.add(f"row{i}")

    # Check columns
    for i in range(5):
        if all(self.Table[j][i] == "*" for j in range(5)):
            self.completed_lines.add(f"col{i}")

    # Check main diagonal
    if all(self.Table[i][i] == "*" for i in range(5)):
        self.completed_lines.add("diag_main")

    # Check anti-diagonal
    if all(self.Table[i][4 - i] == "*" for i in range(5)):
        self.completed_lines.add("diag_anti")

    # If 5 or more unique lines are completed → Bingo
    if len(self.completed_lines) >= 5:
        self.result = True
        return "Bingo"

    return None
        
  def reset_table(self):
       self.Table = [[0 for j in range(5)] for i in range(5)]
       return None
   
class com_bingo(Bingo):
    def get_user_sequence(self):
        used_number=set()
        for i in range (5):
            for j in range(5):
                x=random.randint(1,25)
                if x not in used_number:
                     used_number.add(x)
                     self.Table[i][j]=x
                else:
                    while True:
                       x=random.randint(1,25)
                       if x not in used_number:
                            used_number.add(x)
                            self.Table[i][j]=x 
                            break  
       # self.display()   
       # time.sleep(9)
       # os.system('clear')              
        self.check_winner() 
    
    def  make_predict(self):
        self.check=set()
        for i in range(5):
            count=0
            count = self.Table[i].count("*")
            if count ==4:
                for j in range(5):
                    if self.Table[i][j] != "*":          
                            return self.Table[i][j]
                        
        for i in range(5):
            count=0
            for j in range(5):
                col = [self.Table[r][j] for r in range(5)]
                if col.count("*") == 4:              
                      for i in range(5):
                           if self.Table[i][j] != "*":
                                 return self.Table[i][j]
                        
        for i in range(5):
            count=0
            diag = [self.Table[k][k] for k in range(5)]
            if diag.count("*") == 4:             
                  for i in range(5):
                     if self.Table[i][i] != "*":
                           return self.Table[i][i]
                          
        for i in range(5):
            count=0
            anti = [self.Table[k][4-k] for k in range(5)]
            if anti.count("*") == 4:             
                   for i in range(5):
                       if self.Table[i][4-i] != "*":
                             return self.Table[i][4-i]
       
        while True:
          temp = random.randint(1,25)
          if temp not in self.check:
              return temp
              self.check.add(temp)
              break    
                
            
player1=Bingo()
player2=Bingo() 
player3=Bingo()
computer=com_bingo()

def computer_and_player_num():
    player3.get_user_sequence()
    computer.get_user_sequence()
    single_player_game()
 
 
def computer_disp():
    computer.display()
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")
    
        
def player3_disp():
    player3.display()
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")
    
def single_player_game():
    try:
         while True:
           print("Player :")
           z=input("Do you want to see your table ( y/n):").lower()
           if z == 'y' or z =="yes":
               print("player")
               player3_disp()
           x=int(input("Player 1: Enter number to remove  player 1: "))
           player3.game(x)
           computer.game(x)
           if player3.check_winner():
                 print("player 1 win")
                 player3.reset_table()
                 computer.reset_table()
                 break
           print("computer Turn")
           c=computer.make_predict()
           print(f"computer chosen {c}")
           player3.game(c)
           computer.game(c)
           print("computer")
           computer_disp()
           computer.game(c)
           if computer.check_winner():
               print("Player 2 is winner")
               player3.reset_table()
               computer.reset_table()
               break
               
    except typeError:
       print("Enter valid type data")
    except Exception as e:
       print(e)            
                        
def game_loop():
   try:  
      while True:
          print("Player 1:")
          z=input("Do you want to see your table ( y/n):").lower()
          if z == 'y' or z =="yes":
              player1_disp()
          x=int(input("Player 1: Enter number to remove  player 1: "))
          player1.game(x)
          player2.game(x)
          if player1.check_winner():
             print("player 1 win")
             player1.reset_table()
             player2.reset_table()
             break
          print("Player 2:")
          z=input("Do you want to see your table ( y/n):").lower()
          if z == 'y' or z =="yes":
             player2_disp()
          c=int(input("Player 1: Enter number to remove  player 2: "))
          player1.game(c)
          player2.game(c)
          if player2.check_winner():
              print("Player 2 is winner")
              player1.reset_table()
              player2.reset_table()
              break
              
   except typeError:
       print("Enter valid type data")
       
   except Exception as e:
       print(e)               
          
def player1_disp():
    player1.display()
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")
    
def two_player_mode():
    print("Enter your numbers")
    print("Player 1: Enter your numbers")
    player1.get_user_sequence()
    print("Player 2: Enter your numbers")
    player2.get_user_sequence()
    game_loop()     

def player2_disp():
    player2.display()
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")             
         
if __name__=="__main__":
  while True:
    print("\n======Welcome to Bingo game======")
    print("1. opponent : computer")
    print("2. Opponent : friend")
    print("3. exit")
    x=input("Enter your choice:")
    if x == '1':
        computer_and_player_num()
    elif x == '2':
        two_player_mode()
            
    elif x == '3':
        print("Exiting program....")
        exit(0)
        
    elif x == " ":
        print("You entered space")   
           
    else:
        print("Enter valid input")
