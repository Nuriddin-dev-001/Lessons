import random

board = [" " for _ in range(9)]

def draw_board():
    print(f"""
     {board[0]} | {board[1]} | {board[2]} 
    ---+---+---
     {board[3]} | {board[4]} | {board[5]} 
    ---+---+---
     {board[6]} | {board[7]} | {board[8]} 
    """)

def check_winner():
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Gorizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertikal
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] and board[pos[0]] != " ":
            return board[pos[0]]
    return None

while True:
    draw_board()
    print("Sizning navbatingiz! (X)")

    move = int(input("1-9 oralig'ida katak raqamini kiriting: ")) - 1

    if 0 <= move < 9 and board[move] == " ":
        board[move] = "X"
        winner = check_winner()
        if winner:
            draw_board()
            print(f"Tabriklayman siz g'olibsiz: {winner}!")
            break

        print("Kompyuterning navbati! (0)")
        while True:
            comp_move = random.randint(0, 8)
            if board[comp_move] == " ":
                board[comp_move] = "0"
                break

        winner = check_winner()
        if winner:
            draw_board()
            print(f"G'olib: {winner}!")
            break
    else:
        print("Noto'g'ri tanlov yoki band joy! Qaytadan urinib ko'ring.")

    if " " not in board:
        draw_board()
        print("Durang! O'yin tugadi.")
        break