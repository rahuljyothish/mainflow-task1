# Task-1: Sum of two numbers
def sum_of_two_numbers(a,b):
    return a + b
#example
a,b = 5, 10
print(f"Sum of {a} and {b} is {sum_of_two_numbers(a,b)}.")


#odd or even
number=int(input("enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# factorial calculation
n = int(input("Enter a number: "))
#Initialize
factorial = 1
if n < 0:
    print("factorial is not defined for negative numbers")
else:
    for i in range(1, n+1):
        factorial *= i
        print("The factorial of", n, "is:", factorial)


#Fibonacci Sequence
def fibonacci_sequence(n):
    sequence = [0,1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
#example
n = 10
print(f"the first {n} fibonnaci numbers are: {fibonacci_sequence(n)}")


# reverse a string
def reverse_string(s):
    return s[::-1]
#example
string = "hello"
print(f"the reverse string of '{string}' is {reverse_string(string)}")


#palindrome check
def is_palindrome(s):
    return s == s[::-1]
string = "madam"
print(f"Is '{string}' a palindrome? {is_palindrome(string)}")


#leap year check
def is_leap_year(year):
    #leap year if divisible by 4 and (not divisible by 100 or divisible by 400)
    return(year % 4 == 0) and (year % 100 != 0 or year % 400 ==0)
#example
year = 2024
print(f"Is '{year} a leap year? {is_leap_year(year)}'")


#armstrong number
def is_armstrong_number(n):
    digits = str(n)
    return n == sum(int(d) ** len(digits) for d in digits)
#example
num = 153
print(f"Is {num} an Armstrong number? {is_armstrong_number(num)}")


#custom encryption-decryption system
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

#example
message = "Hello World!"
shift_key = 3

encrypted_message = encrypt(message, shift_key)
decrypted_message = decrypt(encrypted_message, shift_key)

print(f"Original: {message}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")