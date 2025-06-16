#task 2
# Prime number
'''import math
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


#gcd and lcm
import math
def compute_gcd_lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    return gcd, lcm
# Example
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gcd, lcm = compute_gcd_lcm(a, b)
print("GCD", gcd)
print("LCM", lcm)


#reverse list
def reverse_list(lst):
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]
    return lst
# Example
lst = [1, 2, 3, 4, 5]
print("Original list:", lst)
print("Reversed list:", reverse_list(lst))


#bubble sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
# Example
lst = [64, 25, 12, 22, 11]
print("Original list:", lst)
print("Sorted list:", bubble_sort(lst))


#duplicate list
def duplicate_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique
# Example
lst = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", lst)
print("List after removing duplicates:", duplicate_list(lst))


# string length
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
#example
s = input("enter a string: ")
print("Length of the string:", string_length(s))


# vowels and consonants
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    count_vowels = 0
    count_consonants = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                count_vowels += 1
            else:
                count_consonants += 1
                
    return count_vowels, count_consonants
#example
s = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(s)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)'''


# maze 
import random
from collections import deque

ROWS = 21
COLS = 21

def init_maze(rows, cols):
    return [['1' for _ in range(cols)] for _ in range(rows)]

def generated_maze(maze):
    def carve(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < ROWS - 1 and 1 <= ny < COLS - 1 and maze[nx][ny] == '1':
                maze[nx][ny] = '0'
                maze[x + dx // 2][y + dy // 2] = '0'
                carve(nx, ny)

    carve(1, 1)
    maze[1][1] = 'S'
    maze[ROWS - 2][COLS - 2] = 'E'

def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def solved_maze(maze):
    start = end = None
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    if not start or not end:
        print("Start or end point missing.")
        return

    queue = deque([start])
    visited = [[False] * COLS for _ in range(ROWS)]
    prev = [[None] * COLS for _ in range(ROWS)]
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and not visited[nx][ny] and maze[nx][ny] in ('0', 'E'):
                visited[nx][ny] = True
                prev[nx][ny] = (x, y)
                queue.append((nx, ny))

    # Backtrack to mark path
    path = []
    at = end
    while at != start:
        if at is None:
            print("No path found!")
            return
        path.append(at)
        at = prev[at[0]][at[1]]

    for x, y in path:
        if maze[x][y] not in ('S', 'E'):
            maze[x][y] = '.'

def main():
    maze = init_maze(ROWS, COLS)
    generated_maze(maze)
    solved_maze(maze)
    print("Solved Maze:\n")
    print_maze(maze)

if __name__ == "__main__":
    main()

