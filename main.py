def fibonacci(n):
    # Initialize the sequence list with the first two Fibonacci numbers
    sequence = [0, 1]
    
    # Handle base cases
    if n == 0:
        return sequence[0]
    elif n == 1:
        return sequence[1]
    
    # Compute Fibonacci numbers iteratively from 2 up to n
    for i in range(2, n + 1):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)
        
    # The nth Fibonacci number is at index n
    return sequence[n]
