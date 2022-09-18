# Write code for algorithm 3 below: Write a function that returns the nth elements in the Fibonacci Sequence.
def nth_sequence(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return nth_sequence(n-1)+nth_sequence(n-2)
        print("2nd fib number:")
        print(nth_sequence(2))
        print("4th fib number:")
        print(nth_sequence(4))
        print("8th fib number:")
        print(nth_sequence(8))