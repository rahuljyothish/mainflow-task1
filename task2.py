#task 2
# Prime number
import math
def is_prime(n):
    if n <=1:
      return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
# Example
n = int(input("Enter a number to check if it is prime: "))
print(is_prime(n))
    

#sum of digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
# Example
n = int(input("Enter a number to calculate the sum of its digits: "))
print(sum_of_digits(n))