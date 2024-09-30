import itertools
import random

def roll_dice(*sides):
  """
  Simulates rolling dice with the specified number of sides.

  Args:
      *sides: A variable number of integers representing the number of sides on each die.

  Returns:
      A dictionary containing the possible outcomes and their probabilities.
  """

  # Calculate the minimum and maximum possible outcomes
  min_outcome = sum(1 for side in sides)
  max_outcome = sum(side for side in sides)

  # Generate all possible combinations of dice rolls
  rolls = itertools.product(*[range(1, side + 1) for side in sides])

  # Count the occurrences of each outcome
  outcomes = {}
  for roll in rolls:
      outcome = sum(roll)
      outcomes[outcome] = outcomes.get(outcome, 0) + 1

  # Calculate the total number of rolls
  total_rolls = len(rolls)

  # Calculate the probability for each outcome
  probabilities = {outcome: count / total_rolls * 100 for outcome, count in outcomes.items()}

  # Print the results in a table
  print("OUTCOME  PROBABILITY")
  for outcome, probability in probabilities.items():
      print(f"{outcome: <8}{probability:.2f}%")

if __name__ == "__main__":
  roll_dice(4, 6, 6)