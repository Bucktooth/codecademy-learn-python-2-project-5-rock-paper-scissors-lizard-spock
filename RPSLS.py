"""
Codecademy - Learn Python 2
Rock Paper Scissors Lizard Spock
"""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]

message = {
  "tie" : "Yawn it's a tie!",
  "won" : "Yay you won!",
  "lost" : "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print "Computer selected: %s" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
    play_RPS()
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  elif user_choice == options[0] and computer_choice == options[3]:
    print message["won"]
  elif user_choice == options[3] and computer_choice == options[4]:
    print message["won"]
  elif user_choice == options[4] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[3]:
    print message["won"]
  elif user_choice == options[3] and computer_choice == options[1]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[4]:
    print message["won"]
  elif user_choice == options[4] and computer_choice == options[0]:
    print message["won"]
  else:
    print message["lost"]

def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, Scissors, Lizard, or Spock: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)

play_RPS()
