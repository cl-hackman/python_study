
spaces = '1a', '2b', '3c', '4d', '5e', '6f', '7g', '8h'
pieces = 'wking', 'bking', 'wbishop', 'bbishop', 'bknight', 'wknight', 'wrook', 'brook', 'bqueen', 'wqueen'
pawns = 'wpawns', 'bblacks'

def isValidChessBoard(board):
    number = 0
    rags = {}
    for b, c in board.items():
        number += 1
        number <= 16
        for c in board.values():
            c == pieces
            for x in c:
                if x == 'wking' and 'bking':
                    return False
                elif c == 'wking' or 'bking':
                    return True
            

print(isValidChessBoard({'1a': 'wking', '4d': 'bking'}))
            