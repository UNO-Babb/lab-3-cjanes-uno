#RPS.py
#Name: Colton Janes
#Date: 02/09/2025 (edits made on 02/11/2025 to add "while True:..." argument to Y/N question in case user doesn't provide "Y" or "N" and to also allow for lowercase entry via .upper().)
#Assignment: Lab 3 - RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  #Create a loop that continues as long as the user wants to play.
  playAgain = "Y"
  while playAgain.upper() == "Y":
    #User can play as many games as they wish.
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice( ["R", "P", "S"])

    #Prompt the user for their RPS selection
    while True:
      player = input("Choose your \"weapon\" (R, P, S): ").upper()
      if player in ["R", "P", "S"]:
        break #break should indicate that the immediate loop is valid and continues post while argument
      else:
        print("Ope, try again. Please enter R, P, or S.")

    #Determine winner and state what happened to the user
    if player == "R":
      print("Player chose Rock")
    elif player == "P":
      print("Player chose Paper")
    else:
      print("Player chose Scissors")

    if computer == "R":
      print("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors")

    if player == "R" and computer == "R":
      print("Ah, a tie!")
      ties = ties + 1
    if player == "R" and computer == "P":
      print("Computer beat you this time.")
      losses = losses + 1
    if player == "R" and computer == "S":
      print("You win!")
      wins = wins + 1
    
    if player == "P" and computer == "R":
      print("You win!")
      wins = wins + 1
    if player == "P" and computer == "P":
      print("Ah, a tie!")
      ties = ties + 1
    if player == "P" and computer == "S":
      print("Computer beat you this time.")
      losses = losses + 1

    if player == "S" and computer == "R":
      print("Computer beat you this time.")
      losses = losses + 1   
    if player == "S" and computer == "P":
      print("You win!")
      wins = wins + 1
    if player == "S" and computer == "S":
      print("Ah, a tie!")
      ties = ties + 1
    
    #Ask the user if they would like to play again.
    while True:
      playAgain = input("Would you like to play again? (Y/N): ").upper()
      if playAgain in ["Y", "N"]:
        break #break should indicate that the immediate loop is valid and continues post while argument
      else:
        print("Ope, try again. Please enter \"Y\" or \"N\".")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
