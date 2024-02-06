import secret_aucArt
import os
import time
print(secret_aucArt.logo)
print("Welcome to secret auction program")

bidders ={}
is_continue = True

while(is_continue == True):
  name = input("What's your name?: ")
  bid = int(input("What's your bid ? : $"))
  bidders[name] = bid
  choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if choice == 'no':
    is_continue = False
  time.sleep(0.1)
  os.system('clear')
  
  
max = 0
winner = ""

for name in bidders:
  if(bidders[name]>max):
    max = bidders[name]
    winner = name 
    
print(f"The winner is {winner} with a bid of ${max}")