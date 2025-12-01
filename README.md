```markdown
# Fibonacci Number Calculator

This project provides a function to calculate the *n*-th Fibonacci number using a dynamic programming approach. The implementation ensures efficient computation without recursion, making it suitable for calculating large Fibonacci numbers.

## Features

- Calculates the *n*-th Fibonacci number.
- Uses an iterative approach with a list to store intermediate results.
- Handles edge cases for `n = 0` and `n = 1`.

## Usage

### Function Definition

```python
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
        
    # Return the nth Fibonacci number
    return sequence[n]
``

### Example Usage

```python
print(fibonacci(0))   # Output: 0
print(fibonacci(1))   # Output: 1
print(fibonacci(2))   # Output: 1
print(fibonacci(3))   # Output: 2
print(fibonacci(5))   # Output: 5
print(fibonacci(10))  # Output: 55
print(fibonacci(15))  # Output: 610
``

## Testing

This implementation is designed to pass the following tests:

- `fibonacci(0)` returns `0`
- `fibonacci(1)` returns `1`
- `fibonacci(2)` returns `1`
- `fibonacci(3)` returns `2`
- `fibonacci(5)` returns `5`
- `fibonacci(10)` returns `55`
- `fibonacci(15)` returns `610`

## License

This project is for educational purposes and can be freely used and modified.
