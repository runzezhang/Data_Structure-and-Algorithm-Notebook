# Description
# 中文
# English
# Given two integers a and b, an operator, choices:

# +, -, *, /
# Calculate a <operator> b.

# Use switch grammar to solve it

# Have you met this question in a real interview?  
# Example
# Example 1:
# 	Input:  a = 1, b = 2, operator = +
# 	Output: 3
	
# 	Explanation: 
# 	return the result of : 1 + 2.

# Example 2:
# 	Input:  a = 10, b = 20, operator = *
# 	Output: 200
	
# 	Explanation: 
# 	return the result of: 10 * 20.

# Example 3:
# 	Input:  a = 3, b = 2, operator = /
# 	Output: 1
	
# 	Explanation: 
# 	return the result of: 3 / 2.

# Example 4:
# 	Input:  a = 10, b = 11, operator = -
# 	Output: -1
	
# 	Explanation: 
# 	return the result of: 10 - 11.

class Calculator:
    """
    @param a: An integer
    @param operator: A character, +, -, *, /.
    @param b: An integer
    @return: The result
    """
    def calculate(self, a, operator, b):
        # write your code here
        if operator == '+':
            return a + b
        if operator == '-':
            return a - b
        if operator == '*':
            return a * b
        if operator == '/':
            return a // b