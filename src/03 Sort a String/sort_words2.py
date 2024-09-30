def sort_words(string):
  """
  Sorts the words in a string alphabetically.

  Args:
      string: The input string containing words separated by spaces.

  Returns:
      A string containing the sorted words.
  """

  words = string.split()  # Split the string into a list of words
  words.sort()  # Sort the list of words alphabetically
  return ' '.join(words)  # Join the sorted words back into a string

if __name__ == '__main__':
  result = sort_words('banana ORANGE apple')
  print(result)  # Output: apple banana ORANGE