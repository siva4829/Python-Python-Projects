import random as rd
import time

def randomNumbergenerator():
    while True:
        try:
            delay=1
            x = eval(input("Enter one digit number: "))
            time.sleep(delay)
            hell = "0123456789"
            t = rd.choice(hell)
            time.sleep(delay)
            print("the system chosen number is",t)
            
            if x == int(t):
                time.sleep(delay)
                print("Congrats! You're a winner!")
            else:
                time.sleep(delay)
                print("Best of luck for next time!")
            time.sleep(delay)

            v = input("Do you want to try again? (yes/no): ")
            if v == "yes":
                time.sleep(delay)
                continue
            elif v == "no":
                time.sleep(delay)
                print("Thanks for playing!")
                break
            else:
                time.sleep(delay)
                print("Please enter 'yes' or 'no' in lowercase.")
        
        except ValueError:
            print("Please enter a valid number.")

randomNumbergenerator()
