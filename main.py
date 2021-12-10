import random
import math
import time
import os
import sys
from termcolor import colored
#Game Intro
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/75) #0.1/10
def slowprint1(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/500) #0.1/10
again = 1
while (again == 1):
  choice0 = random.randint(1,3)
  print("In this game, you will\nenter your choice of\nRock, Paper, or Scissors\nand compete for the winning spot.")
  print("----------------------------")
  input("Press the ENTER key to begin... ")
  print("----------------------------")
  print()
  print("{:^15}".format("Choice are written down below:"))
  print()
  print("{:^15}{:^15}{:^15}".format("Rock", "Paper", "Scissors"))
  print("{:^15}{:^15}{:^15}".format("1", "2", "3"))
  print()
  while True:
          try:
              choice1 = int(input("Enter the value representing your choice: "))
              while (choice1 < 1 or choice1 > 3):
                print()
                print("----------------------------")
                print()
                print("You did not enter a valid input.")
                print("{:^15}{:^15}{:^15}".format("Rock", "Paper", "Scissors"))
                print("{:^15}{:^15}{:^15}".format("1", "2", "3"))
                choice1 = int(input("Enter the value representing your choice: "))
              break
          except:
              print()
              print("----------------------------")
              print()
              print("You did not enter a valid input.")
              print("{:^15}{:^15}{:^15}".format("Rock", "Paper", "Scissors"))
              print("{:^15}{:^15}{:^15}".format("1", "2", "3"))
              print()
          
  win = 0

  clear = lambda: os.system('clear')
  clear()
  #user
  if(choice1 == 1):
      slowprint("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)
  elif(choice1 == 2):
      slowprint("""
      _______
  ---'    ____)____
            ______)
            _______)
          _______)
  ---.__________)
  """)
  elif(choice1 == 3):
      slowprint("""
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  """)

  print("----------------------------")
  time.sleep(1)
  #computer
  if(choice0 == 1):
      slowprint("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)
  elif(choice0 == 2):
      slowprint("""
      _______
  ---'    ____)____
            ______)
            _______)
          _______)
  ---.__________)
  """)
  elif(choice0 == 3):
      slowprint("""
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  """)
  #Wins
  print("----------------------------")
  time.sleep(1)
  print()
  thing = 0
  if(choice1 == 1 and choice0 == 3):
      thing = 1
  elif(choice1 == 2 and choice0 == 3):
      thing = 3

  #Losses
  if(choice1 == 1 and choice0 == 2): 
      thing = 3
  elif(choice1 == 2 and choice0 == 1):
      thing = 1
  elif(choice1 == 3 and choice0 == 1):
      thing = 3
  elif(choice1 == 3 and choice0 == 2):
      thing = 1

  #Ties
  elif(choice1 == 1 and choice0 == 1):
      thing = 2
  elif(choice1 == 2 and choice0 == 2):
      thing = 2
  elif(choice1 == 3 and choice0 == 3):
      thing = 2

  #results
  if (thing == 1):
      slowprint1(colored("""
  $$\     $$\  $$$$$$\  $$\   $$\       $$\      $$\ $$$$$$\ $$\   $$\ $$\ 
  \$$\   $$  |$$  __$$\ $$ |  $$ |      $$ | $\  $$ |\_$$  _|$$$\  $$ |$$ |
  \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |$$$\ $$ |  $$ |  $$$$\ $$ |$$ |
    \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |  $$ |  $$ $$\$$ |$$ |
    \$$  /   $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |  $$ |  $$ \$$$$ |\__|
      $$ |    $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |  $$ |  $$ |\$$$ |    
      $$ |     $$$$$$  |\$$$$$$  |      $$  /   \$$ |$$$$$$\ $$ | \$$ |$$\ 
      \__|     \______/  \______/       \__/     \__|\______|\__|  \__|\__|
  """, 'red'))
  elif (thing == 3):
      slowprint1(colored("""
  $$\     $$\  $$$$$$\  $$\   $$\       $$\       $$$$$$\   $$$$$$\  $$$$$$$$\ $$\ 
  \$$\   $$  |$$  __$$\ $$ |  $$ |      $$ |     $$  __$$\ $$  __$$\ $$  _____|$$ |
  \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |     $$ /  $$ |$$ /  \__|$$ |      $$ |
    \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |\$$$$$$\  $$$$$\    $$ |
    \$$  /   $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ | \____$$\ $$  __|   \__|
      $$ |    $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |$$\   $$ |$$ |          
      $$ |     $$$$$$  |\$$$$$$  |      $$$$$$$$\ $$$$$$  |\$$$$$$  |$$$$$$$$\ $$\ 
      \__|     \______/  \______/       \________|\______/  \______/ \________|\__|
                                                                                  
  """, 'red'))
  elif (thing == 2):
      slowprint1(colored("""
  $$\     $$\  $$$$$$\  $$\   $$\       $$$$$$$$\ $$$$$$\ $$$$$$$$\ $$$$$$$\  $$\ 
  \$$\   $$  |$$  __$$\ $$ |  $$ |      \__$$  __|\_$$  _|$$  _____|$$  __$$\ $$ |
  \$$\ $$  / $$ /  $$ |$$ |  $$ |         $$ |     $$ |  $$ |      $$ |  $$ |$$ |
    \$$$$  /  $$ |  $$ |$$ |  $$ |         $$ |     $$ |  $$$$$\    $$ |  $$ |$$ |
    \$$  /   $$ |  $$ |$$ |  $$ |         $$ |     $$ |  $$  __|   $$ |  $$ |\__|
      $$ |    $$ |  $$ |$$ |  $$ |         $$ |     $$ |  $$ |      $$ |  $$ |    
      $$ |     $$$$$$  |\$$$$$$  |         $$ |   $$$$$$\ $$$$$$$$\ $$$$$$$  |$$\ 
      \__|     \______/  \______/          \__|   \______|\________|\_______/ \__|
                                                                                  
  """, 'red'))
    
  print()
  print("----------------------------")
  print()
  again = input("Would you like to play again? (Y/N): ").upper()
  while (again != "Y" and again != "N"):
    print()
    print("You did not enter a valid input.")
    time.sleep(1)
    print()
    again = input("Would you like to play again? (Y/N): ").upper()
  if (again == "Y"):
    again = 1
  else:
    again = 2
  clear()
print("""

  _____ _              _          __                _           _           _ 
 |_   _| |_  __ _ _ _ | |__ ___  / _|___ _ _   _ __| |__ _ _  _(_)_ _  __ _| |
   | | | ' \/ _` | ' \| / /(_-< |  _/ _ \ '_| | '_ \ / _` | || | | ' \/ _` |_|
   |_| |_||_\__,_|_||_|_\_\/__/ |_| \___/_|   | .__/_\__,_|\_, |_|_||_\__, (_)
                                              |_|          |__/       |___/   

""")
slowprint1('''
                              _.-="_-         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [w] : /        \ : |========================|    : /        \ :  [w] :
V___________:|          |: |========================|    :|          |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"
''')