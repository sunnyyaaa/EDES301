# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Simple Calculator
--------------------------------------------------------------------------
License:   
Copyright 2026 - <NAME>

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple calculator that will 
  - Take in two numbers from the user
  - Take in an operator from the user
  - Perform the mathematical operation and provide the number to the user
  - Repeat

Operations:
  - "+" : addition
  - "-" : subtraction
  - "*" : multiplication
  - "/" : division
  - ">>" : right shift (integers only)
  - "<<" : left shift (integers only)
  - "%"  : modulo
  - "**" : exponentiation

Error conditions:
  - Invalid operator --> Program should exit
  - Invalid number   --> Program should exit

--------------------------------------------------------------------------
"""

# NOTE - Add import statements to allow access to Python library functions
# NOTE - Hint:  Look at  https://docs.python.org/3/library/operator.html

import operator

try:
    user_input = raw_input
    
except NameError:
    user_input = input
# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# NOTE - No constants are needed for this example 

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# NOTE - Global variable to map an operator string (e.g. "+") to 
# NOTE - the appropriate function.
operators = {
    # Dictionary syntax:  "key" : "value"
    #   i.e. "function" : operator.<function>
    "+" : operator.add,
    "-" : operator.sub,
    "/" : operator.truediv,
    "*" : operator.mul,
    ">>": operator.rshift,
    "<<": operator.lshift,
    "%" : operator.mod,
    "**": operator.pow
}



# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

def get_user_input():
    """ Get input from the user.
        Returns tuple:  (number, number, function) or 
                        (None, None, None) if inputs invalid
    """
    # NOTE - Use "try"/"except" statements to allow code to handle errors gracefully.      
    try:
        text1 = user_input("Enter first number:")
        text2 = user_input("Enter second number:")
        op    = user_input("Enter operation (+, -, *, /, >>, <<, %, **):").strip()
        
        operation = operators[op]
        
        if op in (">>", "<<"):
            num1 = int(text1)
            num2 = int(text2)
            
            if num2 < 0:
                raise ValueError("Shift count cannot be negative")
        
        else:
            num1 = float(text1)
            num2 = float(text2)
                
       
        return (num1, num2, operation)
        # # NOTE - Use "pass" statements to allow code to be run without having to 
        # # NOTE - fill out the contents.  This pass statement should be removed    
        # pass
        
        # NOTE - User input is generally returned as a string and must be translated.
    except (ValueError, KeyError):
        print("Invalid Input")
        return (None, None, None)

# End def



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

# NOTE - The python variable "__name__" is provided by the language and can 
# NOTE - be used to determine how the file is being executed.  For example,
# NOTE - if the program is being executed on the command line:
# NOTE -   python3 simple_calc.py
# NOTE - then the "__name__" will be the string:  "__main__".  If the file 
# NOTE - is being imported into another python file:
# NOTE -   import simple_calc
# NOTE - the the "__name__" will be the module name, i.e. the string "simple_calc"

if __name__ == "__main__":

    # NOTE - Need to add main calculator functionality:
    # NOTE -   - Use a loop construct to repeat the operation
    # NOTE -   - Get the input from the user (i.e. use function created above)    
    # NOTE -   - Check that all inputs are valid (exit the program if inputs invalid)
    # NOTE -   - Execute the function on the numbers and print the results
    while (1):
    
        (n1, n2, op) = get_user_input()
        
        
        if (n1 is None) or (n2 is None) or (op is None):
            print("ERROR: User Input Invalid: {0} {1} {2}\n".format(n1, n2, op))
            exit()
            
        else:
        
            print(op(n1, n2))
        
        
    # print(n1)
    # print(n2)
    # print(op)
    
    # NOTE - Use "pass" statements to allow code to be run without having to 
    # NOTE - fill out the contents.  This pass statement should be removed    
    pass

