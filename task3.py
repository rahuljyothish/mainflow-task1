#Task 3
#table of a number

'''def multiplication_table(n, limit=10):
     for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = 5
multiplication_table(n)

#Swap two numbers

def swap_numbers(a, b) :
    a, b = b, a
    print(f"After swapping: a = {a} , b = {b}")

a, b = 3, 7
swap_numbers(a, b)


#check substring
def is_substring(s1, s2):
    return s2 in s1

s1 = "hello world"
s2 = "world"
print(f"Is '{s2}' a substring of '{s1}'? {is_substring(s1, s2)}")


#Decimal to Binary
def decimal_to_binary(n):
    return bin(n)[2:]

n = 10
print(f"Binary representation of {n}: {decimal_to_binary(n)}")


#Matrix Addition
def add_matrices(a, b):
    result =[[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    return result


a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print("Matrix Addition Result:")
print(add_matrices(a, b))
A = [
    [1, 2],
    [3, 4]
]
B = [
    [5, 6],
    [7, 8]
]

rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

if cols_A != rows_B:
    print("Matrix multiplication not possible: Columns of A must equal rows of B.")
else:
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B
                result[i][j] += A[i][k] * B[k][j]

    print("Product Matrix (A x B):")
    for row in result:
        print(row)


#Find Second Largest
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None


lst = [10,20,20,30]
print(f"Second largest number: {second_largest(lst)}")

#check Anagram
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example
s1 = "listen"
s2 = "silent"
print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams(s1, s2)}")'''


# Initialize board with 9 empty spaces
board = [" "]*9


def show():
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()


def check_win(p):
    win = [(0,1,2), (3,4,5), (6,7,8),
           (0,3,6), (1,4,7), (2,5,8),
           (0,4,8), (2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in win)


def minimax(turn):
    if check_win("O"): return 1
    if check_win("X"): return -1
    if " " not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = turn
            score = minimax("X" if turn == "O" else "O")
            board[i] = " "
            scores.append(score)

    return max(scores) if turn == "O" else min(scores)


def ai_move():
    best = -100
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax("X")
            board[i] = " "
            if score > best:
                best = score
                move = i
    board[move] = "O"


def player_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Already taken!")
        except:
            print("Invalid input!")


def play():
    print("You: X  |  Computer: O")
    show()
    while True:
        player_move()
        show()
        if check_win("X"):
            print("You win!")
            break
        if " " not in board:
            print("Draw!")
            break

        print("Computer's turn...")
        ai_move()
        show()
        if check_win("O"):
            print("Computer wins!")
            break
        if " " not in board:
            print("Draw!")
            break

play()
