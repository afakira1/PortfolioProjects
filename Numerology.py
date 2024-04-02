'''
 
@author: Amer Fakira
Program Name: Numerology
Program Description: This assignment uses Numerology to assign numerical values to words. 
The program will read in a .txt file, and will create a dictionary to show the word list
values sorted by word, word lists by value, and the key values with the most words.
'''
# Importing string and punctuation for necessary cleaning
import string
from string import punctuation

def processData():

    my_file = open("gettysburg.txt", "r")
    content = my_file.read()
    my_file.close
    
    # Remove punctuation using string translation
    table = str.maketrans('', '', string.punctuation) # Creating a translation table to map characters to replacement characters
    cleaned_text = content.translate(table)
    return cleaned_text.lower()  # Lowercase the text after cleaning
    


# Creating the numerology calculation function
def numerology(text):
  
  # Creating a dictionary to map letters to their numerology values
  letter_values = {chr(i): i - 96 for i in range(97, 123)}

  words = text.split()

  # Calculating the numerology value for each word
  word_values = {}
  for word in words:
    value = 0
    for letter in word:
      if letter in letter_values:
        value += letter_values[letter]
    word_values[word] = value

  return word_values


text = processData()  
word_values = numerology(text)


# Creating the dictionary to store the numerology value of each word in the file
def createWordValueDict(text):
  
  # Calling the numerology function to calculate the different word values
  word_values = numerology(text)
  return word_values


text = processData()  
word_values = createWordValueDict(text)


# Creating the dictionary to have each key value and the list of words with that value (no repeats)
def createKeyWordDict(word_value_dict):


  # Creating an empty dictionary to store numerology word mappings
  key_word_dict = {}

  # Iterating through each word value pair in the dictionary
  for word, value in word_value_dict.items():
    # Checking if the numerology value exists as a key in the dictionary
    if value in key_word_dict:
      # Appending the word to the list of words with that value if the value exists (avoiding duplicates)
      if word not in key_word_dict[value]:
        key_word_dict[value].append(word)
    else:
      # Creating a new list for words with that value and add the first word if the value is new
      key_word_dict[value] = [word]

  return key_word_dict


text = processData()  
word_values = createWordValueDict(text)
key_word_dict = createKeyWordDict(word_values)


# Creating the arrange function to arrange the key values in increasing order
def arrange(d):


  # Sorting the dictionary by key in ascending order
  sorted_items = sorted(d.items())

  # Printing each key and value pair with sorted values
  for key, value in sorted_items:
    if isinstance(value, int):  # Checking if the value is an integer (for word_values)
      print(f"{key: >11} : {value}") #right-aligning the words/keys
    else:
      print(f"{key: >3} : {sorted(value)}")  #Sorting the values for other dictionaries, and right-aligning the words/key values

    
text = processData()  
word_values = createWordValueDict(text)
key_word_dict = createKeyWordDict(word_values)

# Arranging and printing the word and value dictionary (sorted by numerology value)
print("Word List Values (Sorted By Word):")
print(f'{"="*34}')
arrange(word_values)

# Arranging and printing the key word dictionary (sorted by numerology value, then words within each value)
print("\nWord Lists by Value:")
print(f'{"="*20}')
arrange(key_word_dict)

# Creating the mostWords function to find numerology values with the greatest number of words associated with them
def mostWords(d, output_filename="output.txt"):
  

  # Initializing variables to track most frequent values
  max_count = 0
  most_frequent_values = []

  # Iterating through each numerology value/key and its total word list/value
  for value, word_list in d.items():
    # Getting the current word count for this numerology value
    current_count = len(word_list)

    # Checking if new maximum count of words list is found
    if current_count > max_count:
      # Clearing the previous most frequent values and updating the max count if necessary
      max_count = current_count
      most_frequent_values = [value]
    elif current_count == max_count:
      # Adding the current value to the list if there's a tie
      most_frequent_values.append(value)

  # Printing the results to the console
  print(f"\nMost Words: {max_count}")
  print(f"{'='*63}")
  
  for value in sorted(most_frequent_values):
    print(f"{value}: {sorted(d[value])}")

  # Writing the results to an output file
  with open(output_filename, "w") as outfile:
    outfile.write(f"Most Words: {max_count}\n")
    outfile.write(f"Numerology Values: {sorted(most_frequent_values)}\n")
    for value in sorted(most_frequent_values):
      outfile.write(f"\t- Words with value {value}: {sorted(d[value])}\n")

text = processData()  
word_values = createWordValueDict(text)
key_word_dict = createKeyWordDict(word_values)

mostWords(key_word_dict)

# Creating the main function to make calls to all other functions created
def main():
    
    text = processData()
    word_values = createWordValueDict(text)
    key_word_dict = createKeyWordDict(word_values)

    # Printing the sorted word-value dictionary
    print("Word List Values (Sorted By Word):")
    print(f'{"="*34}')
    arrange(word_values)

    # Printing the sorted key-word dictionary
    print("\nWord Lists by Value:")
    print(f'{"="*20}')
    arrange(key_word_dict)

    # Finding and printing/writing the numerology values with most associated words
    mostWords(key_word_dict)


