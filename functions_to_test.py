# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return a + b

def find_maximum(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and  c > b:
        return c

def is_palindrome(string):
    
    string_rev = string[::-1]
    print(f"{string}, {string_rev}")
    if string_rev == string:
        print("Is palindrome")
        return True
        
def count_word_occurrences(text, word):
    
    count = 0 
    text = text.split()
    
    for chars in text:
        if word == chars:
            count += 1
    # print(count)
    return count

def read_file_lines(filepath):
    with open(filepath, 'r') as file_to_read:
        file_reader = file_to_read.readlines()
        print(file_reader)

def factorial(n):
    pass

def is_prime(n):
    

def sort_numbers(numbers):
    sorted_nums = sorted(numbers)
    print(sorted_nums)

def factorial(n):
    pass

def fibonacci(n):
    pass

def tower_of_hanoi(n, source, auxiliary, target):
    
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    pass

class Person:
    def __init__(self, name, age):
        pass


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g
    print(find_maximum(2, 90, 4))
    print(is_palindrome("mom"))
    print(sort_numbers([1,4,3,6,2]))
    print(count_word_occurrences("I am a little teacup short and stout little little one", "little"))