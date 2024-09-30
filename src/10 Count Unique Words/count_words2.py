from collections import Counter

def count_words(file_path):
  """
  Counts the words in a text file and prints the total count and top 20 most frequent words.

  Args:
      file_path: The path to the text file.
  """

  # Open the file and read its contents
  with open(file_path, 'r') as f:
      text = f.read().lower()

  # Split the text into words, removing non-alphanumeric characters
  words = [word for word in text.split() if word.isalnum()]

  # Count word occurrences using Counter
  word_counts = Counter(words)

  # Print the total number of words
  print(f"Total Words: {len(words)}")

  # Get the top 20 most frequent words
  top_20_words = word_counts.most_common(20)

  # Print the top 20 words and their counts in a table
  print("\nTop 20 Words:")
  print("{: <8} {: >6}".format("WORD", "COUNT"))
  for word, count in top_20_words:
      print(f"{word: <8} {count: >6}")

if __name__ == "__main__":
  file_path = "shakespeare.txt"  # Replace with your actual file path
  count_words(file_path)