#RPS.py
#Name: Colton Janes
#Date: 02/09/2025
#Assignment: Lab 3 - RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  playAgain = "Y"
  while playAgain == "Y":
    #User can play as many games as they wish.
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice( ["R", "P", "S"])

    #Prompt the user for their RPS selection
    while True:
      player = input("Choose your \"weapon\" (R, P, S): ").upper()
      if player in ["R", "P", "S"]:
          #look over documentation and see if you need to move the "if player ==" content up to here and be part of the loop
    #End selection loop.

    #Determine winner and state what happened to the user
    if computer == "R":
      print("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors")

    if player == "R":
      print("Player chose Rock")
    elif player == "P":
      print("Player chose Paper")
    else:
      print("Player chose Scissors")

    if player == "R" and computer == "R":
      print("Ah, a tie!")
      ties = ties + 1
    if player == "R" and computer == "P":
      print("Computer beat you this time.")
    if player == "R" and computer == "S":
      print("You win!")
    
    #Ask the user if they would like to play again.
    playAgain = input("Would you like to play again? (Y/N): ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
