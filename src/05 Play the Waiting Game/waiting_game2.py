import random
import time

def waiting_game():
    """
    Plays the waiting game, where the player has to wait a random amount of time.

    Returns:
        None
    """

    # Generate a random target time between 2 and 4 seconds
    target_time = random.randint(2, 4)

    print(f"Your target time is {target_time} seconds")
    print(" ---Press Enter to Begin---")

    input()  # Wait for the player to press Enter

    # Start the timer
    start_time = time.time()

    # Wait for the player to press Enter again
    input()

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Print the elapsed time and the result
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

    if elapsed_time < target_time:
        print(f"({abs(elapsed_time - target_time):.3f} seconds too fast)")
    elif elapsed_time > target_time:
        print(f"({abs(elapsed_time - target_time):.3f} seconds too slow)")
    else:
        print("Right on target!")

if __name__ == "__main__":
    waiting_game()