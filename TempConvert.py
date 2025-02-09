#TempConvert.py
#Name: Colton Janes
#Date: 02/09/2025
#Assignment: Lab 3 - TempConvert


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Provide a temperature, assuming it's in Fahrenheit: "))

  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = (tempF - 32) * 5/9
  tempC = round(tempC, 2)

  #Output converted temperature.
  print(tempF, "degrees Fahrenheit is", tempC, "degrees Celsius.")

if __name__ == '__main__':
  main()