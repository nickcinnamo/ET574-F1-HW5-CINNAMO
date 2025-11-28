def factorial(x):
    if type(x) is not int:
        return "Error: Input must be an integer."
    if x < 0:
        return "Error: Input must be a non-negative integer."

    if x == 0:
        return 1

    result = 1
    for i in range(1, x + 1):
        result = result * i
    
    return result

def mean(numbers):
    is_list = type(numbers) is list
    is_tuple = type(numbers) is tuple
    if not (is_list or is_tuple):
        return "Error: Input must be a list or tuple of numbers."
    
    if not numbers:
        return "Error: Input list/tuple cannot be empty."

    total = 0
    for num in numbers:
        is_int = type(num) is int
        is_float = type(num) is float
        if not (is_int or is_float):
            return "Error: All elements in the list/tuple must be numbers."
        total = total + num

    count = 0
    for _ in numbers:
        count = count + 1

    if count == 0:
        return 0 
        
    return total / count

def fibonacci(n):
    if type(n) is not int:
        return "Error: Input must be an integer."
    if n <= 0:
        return "Error: Input must be a positive integer (n >= 1)."
    
    if n == 1:
        return 1
    if n == 2:
        return 1
        
    a = 1
    b = 1
    
    for _ in range(3, n + 1):
        next_fib = a + b
        a = b
        b = next_fib
        
    return b