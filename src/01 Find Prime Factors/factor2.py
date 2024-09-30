def get_prime_factors(number):
  """
  Finds the prime factors of a given number.

  Args:
      number: The input number.

  Returns:
      A list containing the prime factors of the number.
  """

  prime_factors = []
  divisor = 2

  while divisor <= number:
    if number % divisor == 0:
      prime_factors.append(divisor)
      number //= divisor
    else:
      divisor += 1

  return prime_factors

if __name__ == '__main__':
  result = get_prime_factors(630)
  print(result)  # Output: [2, 3, 3, 5, 7]