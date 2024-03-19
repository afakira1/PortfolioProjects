#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: amerfakira



The purpose of this program is to take in a temperature scale to convert FROM, and to convert TO
from the user, and to perform the proper conversion. The program consists of 5 functions (fromTemp(),
toTemp(), calculateTemp(), printResults(), and Main())
"""

def fromTemp():

  # Creating the fromTemp output
  print(f'{"#"*37}')
  print(f'# Temperature Scale to Convert From #')
  print(f'{"#"*37}')
  print(f'(F)ahrenheit Scale')
  print(f'(C)elsius Scale')
  print(f'(K)elvin Scale')
  print(f'(R)ankine Scale')
  print(f'{"="*37}')
  validScales = {"f", "c", "k", "r"} # Creating a set to hold the validScales for user input

  # Creating a while loop to ensure the user input is one of the correct options  
  while True:
    tempSelection = input("Make a selection: ").lower()
    if tempSelection in validScales:
      if tempSelection == 'f':
        return f"Convert FROM Fahrenheit Selected..."
      elif tempSelection == 'c':
        return f"Convert FROM Celsius Selected..."
      elif tempSelection == 'k':
        return f"Convert FROM Kelvin Selected..."
      elif tempSelection == 'r':
        return f"Convert FROM Rankine Selected..."
    else:
      print("Invalid Input...")



def toTemp(fromScale):
    # Passing in the users FROM selection, and creating new valid scales based on the input
  if fromScale == 'fahrenheit':
    validToScales = {"c", "k", "r"}
  elif fromScale == 'celsius':
    validToScales = {"f", "k", "r"}
  elif fromScale == 'kelvin':
    validToScales = {"f", "c", "r"}
  else:
    validToScales = {"f", "c", "k"}
    # Creating a while loop to ensure the user is inputting a valid option to convert TO
  while True:
    print(f'\n{"#"*37}')
    print(f'# Temperature Scale to Convert To #')
    print(f'{"#"*37}')
    # Creating the proper TO table, accounting for the users FROM selection
    if fromScale == 'fahrenheit':
        print(f'(C)elsius Scale')
        print(f'(K)elvin Scale')
        print(f'(R)ankine Scale')
    elif fromScale == 'celsius':
        print(f'(F)ahrenheit Scale')
        print(f'(K)elvin Scale')
        print(f'(R)ankine Scale')
    elif fromScale == 'kelvin':
        print(f'(F)ahrenheit Scale')
        print(f'(C)elsius Scale')
        print(f'(R)ankine Scale')
    else:
        print(f'(F)ahrenheit Scale')
        print(f'(C)elsius Scale')
        print(f'(K)elvin Scale')
    print(f'{"="*37}')
    tempToSelection = input("Make a selection: ").lower() # Asking user for TO selection
    if tempToSelection in validToScales:
      if tempToSelection == 'f':
        return f"Convert TO Fahrenheit Selected..."
      elif tempToSelection == 'c':
        return f"Convert TO Celsius Selected..."
      elif tempToSelection == 'k':
        return f"Convert TO Kelvin Selected..."
      elif tempToSelection == 'r':
        return f"Convert TO Rankine Selected..."
    else:
      print("Invalid Input...")


#fromScale = result.split()[2].lower() # Splitting the sentence of fromTemp based on white spaces, and selecting the third word.
#toResult = toTemp(fromScale)
#print(toResult)

# Creating the calculate function
def calculateTemp(fromValue, toValue):
    temperature = eval(input(f'Enter a {fromValue} Temperature Value to Convert: '))
    print(f"\n{fromValue[0].upper()+fromValue[1:]} Conversion to {toValue[0].upper()+toValue[1:]}")
    if fromValue == 'fahrenheit':
        if toValue == 'celsius':
            conversion = (temperature - 32) * (5/9)
            return f"{temperature:.2f} F = {conversion:.2f} C"
        elif toValue == 'kelvin':
            conversion = (temperature + 459.67) * (5/9)
            return f"{temperature:.2f} F = {conversion:.2f} K"
        elif toValue == 'rankine':
            conversion = temperature + 459.67
            return f"{temperature:.2f} F = {conversion:.2f} R"
    elif fromValue == 'celsius':
        if toValue == 'fahrenheit':
            conversion = temperature * (9/5) + 32
            return f"{temperature:.2f} C = {conversion:.2f} F"
        elif toValue == 'kelvin':
            conversion = temperature + 273.15
            return f"{temperature:.2f} C = {conversion:.2f} K"
        elif toValue == 'rankine':
            conversion = (temperature + 273.15) * (9/5)
            return f"{temperature:.2f} C = {conversion:.2f} R"
    elif fromValue == 'kelvin':
        if toValue == 'fahrenheit':
            conversion = temperature * (9/5) - 459.67
            return f"{temperature:.2f} K = {conversion:.2f} F"
        elif toValue == 'celsius':
            conversion = temperature - 273.15
            return f"{temperature:.2f} K = {conversion:.2f} C"
        elif toValue == 'rankine':
            conversion = temperature * (9/5)
            return f"{temperature:.2f} K = {conversion:.2f} R"
    else:
        if toValue == 'fahrenheit':
            conversion = temperature - 459.67
            return f"{temperature:.2f} R = {conversion:.2f} F"
        elif toValue == 'celsius':
            conversion = (temperature - 491.67) * (5/9)
            return f"{temperature:.2f} R = {conversion:.2f} C"
        elif toValue == 'kelvin':
            conversion = temperature * (5/9)
            return f"{temperature:.2f} R = {conversion:.2f} K"
            
    
    
#fromValue = fromScale
#toValue = toResult.split()[2].lower()
#conversionResult = calculateTemp(fromValue,toValue)
#print(conversionResult)


def printResults(fromValue,toValue,conversionResult):
    return f"{conversionResult}"
    
#finalOutput = printResults(fromValue,toValue,conversionResult)   
#print(finalOutput) 


# Creating the main function to call all other functions
def main():
    
    while True:
    
        fromResult = fromTemp()
        fromScale = fromResult.split()[2].lower()
        print(fromResult)

        toResult = toTemp(fromScale)
        toScale = toResult.split()[2].lower()
        print(toResult)

        conversionResult = calculateTemp(fromScale, toScale)
        final_output = printResults(fromScale, toScale, conversionResult)
        print(final_output)
        #print(conversionResult)
        
        answer = input("\nDo you want to do another conversion? (y/n): ").lower()
        # Creating the repeat/break part of the program
        if answer not in ("y", "yes"):
            print("Terminating program...")
            break

main()
