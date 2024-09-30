def is_palindrome(text):
  """
  Checks if a given text string is a palindrome.

  Args:
      text: The input text string.

  Returns:
      True if the text is a palindrome, False otherwise.
  """

  # Remove non-alphanumeric characters and convert to lowercase
  text = ''.join(char.lower() for char in text if char.isalnum())

  # Compare the text with its reversed version
  return text == text[::-1]

if __name__ == '__main__':
  result1 = is_palindrome('hello world')
  print(result1)  # Output: False

  result2 = is_palindrome('Go hang a salami, I’m a lasagna hog.')
  print(result2)  # Output: True