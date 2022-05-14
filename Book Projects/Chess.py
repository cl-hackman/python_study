board = {
    "1a": "wrook", "1b": "wknight", "1c": "wbishop", "1d": "wqueen",
    "1e": "wking", "1f": "wbishop", "1g": "wknight", "1h": "wrook",
    "2a": "wpawn", "2b": "wpawn", "2c": "wpawn", "2d": "wpawn",
    "2e": "wpawn", "2f": "wpawn", "2g": "wpawn", "2h": "wpawn",
    "8a": "brook", "8b": "bknight", "8c": "bbishop", "8d": "bqueen",
    "8e": "bking", "8f": "bbishop", "8g": "bknight", "8h": "brook",
    "7a": "bpawn", "7b": "bpawn", "7c": "bpawn", "7d": "bpawn",
    "7e": "bpawn", "7f": "bpawn", "7g": "bpawn", "7h": "bpawn",
}


def ValidChessBoard(chess_board):

   # Line of code to check whether there is one black king and one white king
    if "bking" not in chess_board.values() or "wking" not in chess_board.values():
        return False

    # Code to check whether each player has only maximum of 16 pieces
    blk = 0  # Initialize black pieces to 0
    wht = 0  # Initialize white pieces to 0
    for clr in chess_board.values():
        if clr[0] == "b":
            blk += 1
        elif clr[0] == "w":
            wht += 1
    if blk >= 17 or wht >= 17:  # If the above provided condition is violated then it returns False value
        return False

    # Code to know each player has atmost 8 pawns
    if sum(i == "bpawn" for i in chess_board.values()) >= 9 or sum(i == "wpawn" for i in chess_board.values()) >= 9:
        # If the condition is violated then False is returned
        return False

    # Code for checking validity
    brd_k = list(chess_board)  # Code for creation of list of dictionary keys
    y = ["1", "2", "3", "4", "5", "6", "7", "8"]
    brd_y = [s[:1] for s in brd_k]  # Line for removal of letters
    # checks if all values from brd_y are in the y-list
    if not all(element in y for element in brd_y):
        # If the values are not present in y_list which are present in brd_y then False is returned
        return False

    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    brd_x = [s[1:] for s in brd_k]  # Line of code for removal of numbers
    if not all(element in x for element in brd_x):
        # If the values are not present in x_list which are present in brd_x then False is returned
        return False

    # Line of code to check whether it starts with the character "w" or "b"
    for pcs in chess_board.values():
        if pcs[0] != "b" and pcs[0] != "w":
            return False

    # Code to check if the piece names are valid or not
    pcs_nms = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    for nms in chess_board.values():
        if nms[1:] not in pcs_nms:
            return False
    return True
