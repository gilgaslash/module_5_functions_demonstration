"""
Description: Module 05 demonstration: Functions
Author: Gilga Mesh
Date: 23/10/2023
Usage: To run individual functions, place a function 
call within the main guard.
"""

def greet()->None:
    """
    Prints a greeting to the console.
    Returns:
        None
    """
    print("Konichiwa World!")
    

def greet_name_age(name: str, age: int)->None:
    """
    Prints a greeting which includes name and age values.
    Args:
        name (str): The name of the person being greeted.
        age (int): The age of the person being greeted.
    Returns:
        None
    """
    print(f"Hello {name}, you are {age} years old")



def math_operation(operand_1: int, operand_2: int, operator: str)->float:
    """
    Returns the result of the specified operations on the operand.
    Args:
        operand_1 (int): left side operand.
        operand_2 (int): right side operand.
    Returns:
        float: The result of the operation.
    Raises:
        ValueError: Invalid operation: please use + or - .
            occurs when an operator other than + or - is provided.
    """
    if operator == "+":
        result = operand_1 + operand_2
    elif operator == "-":
        result = operand_1 - operand_2
    else:
        raise ValueError("Invalid operation: please use + or - .")
    
    return float(result)

try:
    result = math_operation(1, 3, "+") #4.0
    print(result)
except ValueError as e:
    print(e)

try:
    print(math_operation(6, 10, "-"))  #-4
except ValueError as e:
    print(e)


try:
    print(math_operation(5, 5, "*"))   #25.0    actual 0.0
except ValueError as e:
    print(e)
print("End of program.")



print(math_operation.__doc__) #dunder = __ (double underscore)
print(print.__doc__)






















