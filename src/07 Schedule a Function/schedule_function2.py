import sched
import time

def schedule_function(delay, function, *args):
    """
    Schedules a function to be executed after a specified delay.

    Args:
        delay: The delay in seconds before the function is executed.
        function: The function to be executed.
        args: A variable number of arguments to pass to the function.
    """

    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(delay, 1, function, args)
    scheduler.run()

    print(f"{function.__name__} scheduled for {time.ctime(time.time() + delay)}")