import random as rd
import time as t

# Define characters
numbers = "1234567890"
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chars = "~!@#$%^&*()_+,.?/:;'-"

# Functions to generate random passwords 
def generate_numbers(length):
    return ''.join(rd.choices(numbers, k=length))

def generate_alphabets(length):
    return ''.join(rd.choices(alphabets, k=length))

def generate_special_chars(length):
    return ''.join(rd.choices(special_chars, k=length))

def generate_all(length):
    all_chars = numbers + alphabets + special_chars
    return ''.join(rd.choices(all_chars, k=length))

# User Interface
print("\nWelcome to the Random Password Generator")
t.sleep(3)
m = int(input("\nEnter the length of password: "))
t.sleep(3)
print("\nPlease choose the type of password you want:")
print("1. Numbers\n2. Alphabets\n3. Special Characters\n4. Mixed (All)")
t.sleep(3)
c = int(input("\n Enter your choice: "))

if c == 1:
    password = generate_numbers(m)
elif c == 2:
    password = generate_alphabets(m)
elif c == 3:
    password = generate_special_chars(m)
elif c == 4:
    password = generate_all(m)
else:
    print("\nPlease enter a valid input")
    exit()
t.sleep(3)
print("\nYour random password:", password)
t.sleep(2)
print("\nThe program was executed successfully")
