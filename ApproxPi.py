#ApproxPi.py
#Name: Colton Janes
#Date: 02/09/2025
#Assignment: Lab 3 - ApproxPi
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  decimalPi = input("How many decimal points of Pi would you like checked against: ")
  decimalPi = int(decimalPi)

  start = time.time()
  #calculate pi using the approximation technique
  approxPi = 4/1

  sign = -1
  denom = 3

  #Loop until the level of percision is reached
  while round(approxPi, decimalPi) != round(realPi, decimalPi):
    #print(approxPi)
    approxPi = approxPi + (sign * 4 / denom)

    sign = sign * -1
    denom = denom + 2

  end = time.time()
  elapsedTime = end - start

  print("Approximate Pi Value after", decimalPi, "decimal places:",round(approxPi, decimalPi))
  #Considering significant figures here, going to keep same number of decimal pointes as decimalPi
  print("It took", round(elapsedTime, decimalPi), "seconds to calculate this.")


if __name__ == '__main__':
  main()
