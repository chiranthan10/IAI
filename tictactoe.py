def next_move(player, board):
    Empty = '_'
    win = player[0]
    tmarker = 'O' if player[0] == 'X' else 'X'

    if empty_board(board):
        if board[1][1] == Empty:
            print("1 1")
            return
    elif search_board(player[0], board):
        return
    elif search_board(tmarker, board):
        return
    else:
        if board[1][1] == Empty:
            print("1 1")
            return
        elif board[0][0] == Empty:
            print("0 0")
            return
        elif board[0][2] == Empty:
            print("0 2")
            return
        elif board[2][0] == Empty:
            print("2 0")
            return
        elif board[2][2] == Empty:
            print("2 2")
            return

def empty_board(board):
    for row in board:
        for cell in row:
            if cell != '_':
                return False
    return True

def search_board(x, board):
    Empty = '_'
    tmarker = x

    if board[1][1] == tmarker:
        if board[0][1] == tmarker and board[2][1] == Empty:
            print("2 1")
            return True
        elif board[1][0] == tmarker and board[1][2] == Empty:
            print("1 2")
            return True
        elif board[1][2] == tmarker and board[1][0] == Empty:
            print("1 0")
            return True
        elif board[2][1] == tmarker and board[0][1] == Empty:
            print("0 1")
            return True

    if board[0][0] == tmarker:
        if board[0][1] == tmarker and board[0][2] == Empty:
            print("0 2")
            return True
        elif board[1][0] == tmarker and board[2][0] == Empty:
            print("2 0")
            return True
        elif board[1][1] == tmarker and board[2][2] == Empty:
            print("2 2")
            return True
        elif board[2][0] == tmarker and board[1][0] == Empty:
            print("1 0")
            return True
        elif board[0][2] == tmarker and board[0][1] == Empty:
            print("0 1")
            return True
        elif board[2][2] == tmarker and board[1][1] == Empty:
            print("1 1")
            return True

    if board[0][2] == tmarker:
        if board[0][1] == tmarker and board[0][0] == Empty:
            print("0 0")
            return True
        elif board[1][2] == tmarker and board[2][2] == Empty:
            print("2 2")
            return True
        elif board[1][1] == tmarker and board[2][0] == Empty:
            print("2 0")
            return True
        elif board[2][2] == tmarker and board[1][2] == Empty:
            print("1 2")
            return True
        elif board[0][0] == tmarker and board[0][1] == Empty:
            print("0 1")
            return True
        elif board[2][0] == tmarker and board[1][1] == Empty:
            print("1 1")
            return True

    if board[2][0] == tmarker:
        if board[2][1] == tmarker and board[2][2] == Empty:
            print("2 2")
            return True
        elif board[1][0] == tmarker and board[0][0] == Empty:
            print("0 0")
            return True
        elif board[1][1] == tmarker and board[0][2] == Empty:
            print("0 2")
            return True
        elif board[0][0] == tmarker and board[1][0] == Empty:
            print("1 0")
            return True
        elif board[2][2] == tmarker and board[2][1] == Empty:
            print("2 1")
            return True
        elif board[0][2] == tmarker and board[1][1] == Empty:
            print("1 1")
            return True

    if board[2][2] == tmarker:
        if board[1][1] == tmarker and board[0][0] == Empty:
            print("0 0")
            return True
        elif board[2][1] == tmarker and board[2][0] == Empty:
            print("2 0")
            return True
        elif board[1][2] == tmarker and board[0][2] == Empty:
            print("0 2")
            return True
        elif board[0][2] == tmarker and board[1][2] == Empty:
            print("1 2")
            return True
        elif board[2][0] == tmarker and board[2][1] == Empty:
            print("2 1")
            return True
        elif board[0][0] == tmarker and board[1][1] == Empty:
            print("1 1")
            return True

    return False

def main():
    player = input().strip()
    board = [input().strip() for _ in range(3)]
    next_move(player, board)

if __name__ == "__main__":
    main()
