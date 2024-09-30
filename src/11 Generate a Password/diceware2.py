import random

def load_diceware_wordlist(filename="diceware.wordlist.asc"):
  """
  Loads the Diceware wordlist from a file.

  Args:
      filename: The filename of the Diceware wordlist. Defaults to "diceware.wordlist.asc".

  Returns:
      A dictionary where keys are 5-letter strings and values are the corresponding words.
  """
  wordlist = {}
  with open(filename, "r") as f:
    lines = f.readlines()[2:7778]
    for line in lines:
      code, word = line.split()
      wordlist[code] = word
    return wordlist

def generate_passphrase(num_words):
  """
  Generates a passphrase by selecting random words from the Diceware wordlist.

  Args:
      num_words: The number of words to include in the passphrase.

  Returns:
      A string containing a sequence of randomly selected words separated by spaces.
  """
  wordlist = load_diceware_wordlist()
  passphrase = ""
  for _ in range(num_words):
    # Generate a random 5-letter code
    code = "".join(str(random.randint(1, 6)) for _ in range(5))
    passphrase += wordlist[code] + " "
  return passphrase.strip() # Remove trailing space

# Example usage
print(generate_passphrase(4))