def factorial(n):
    """
    This function returns the factorial of a given number.
    
    Parameters:
    n (int): The number to calculate the factorial of. Must be a non-negative integer.
    
    Returns:
    int: The factorial of the given number.
    
    Explanation:
    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    It is denoted by n! and is defined as:
    - 0! = 1 (by definition)
    - n! = n * (n-1) * (n-2) * ... * 1 for n > 0
    
    This function uses a recursive approach:
    - If n is 0, it returns 1 (base case).
    - Otherwise, it returns n multiplied by the factorial of (n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)