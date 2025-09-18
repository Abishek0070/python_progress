def fibonacci_sequence():
    """
    Generates and prints the first N terms of the Fibonacci sequence.
    """

    # Get the number of terms N from the user
    try:
        N = int(input())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Handle the base cases
    if N <= 0:
        return  # No output for N <= 0
    elif N == 1:
        print(0)
        return
    
    # Initialize the first two terms of the sequence
    a, b = 0, 1
    
    # Print the first two terms
    print(a, b, end=" ")
    
    # Loop N-2 times to generate the remaining terms
    for _ in range(2, N):
        # Calculate the next term
        c = a + b
        # Print the next term
        print(c, end=" ")
        # Update the terms for the next iteration
        a = b
        b = c

# Run the function to generate the sequence
fibonacci_sequence()