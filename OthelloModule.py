##### This module implement the game logic plus the class "Othello", which is a
##### game object type


BLACK = '*'
WHITE = 'o'
EMPTY = '.'


class InvalidColorError(Exception):
    """Raises an error when the user input any color other than black or white"""
    pass

class OthelloIndexError(Exception):
    """Raises an error when the user input an invalid range"""
    pass

class OthelloInvalidRowColumn(Exception):
    """Raises an error when the user set up an invalid board"""
    pass

class Othello():
    def __init__(self, columns: int, rows: int, turn: str, top_left: str):
        """
        Initiates the number of columns, rows, board and turn by promting
        the user to input
        """
        self._NUMBER_OF_COLUMNS = columns
        self._NUMBER_OF_ROWS = rows
        self._board = _new_game_board(self._NUMBER_OF_COLUMNS, self._NUMBER_OF_ROWS, top_left)
        self._turn = turn

    def show_rows(self) -> int:
        """
        Returns the number of rows
        """
        return self._NUMBER_OF_ROWS

    def show_columns(self) -> int:
        """
        Returns the number of columns
        """
        return self._NUMBER_OF_COLUMNS
        
    def listboard(self) -> [list]:
        """
        Returns the board as a 2D list
        """ 
        return self._board
    
    def niceboard(self) -> "board":
        """
        Returns the board with a nicely set up
        """
        return set_up(self._board, self._NUMBER_OF_ROWS, self._NUMBER_OF_COLUMNS)

    def turn(self) -> "turn":
        """
        Returns the current turn. If the current turn doesn't have an invalid
        move, it will switch to the other player. If both players doesn't have
        any valid move, returns EMPTY (none of the player will make the move,
        the game is over in this case)
        """
        count = 0
        check_current_turn = _check_every_piece(self._NUMBER_OF_COLUMNS, self._NUMBER_OF_ROWS, self._board, self._turn)
        if check_current_turn == []:
            count += 1
            check_next_turn = _check_every_piece(self._NUMBER_OF_COLUMNS, self._NUMBER_OF_ROWS, self._board, _opposite_turn(self._turn))
            if check_next_turn == []:
                count += 1
        if count == 1:
            self._turn = _opposite_turn(self._turn)
        elif count == 2:
            self._turn = EMPTY
        return self._turn

    def drop(self, col, row) -> None:
        """
        Asks the user to input the coordinate of the piece, drop it, then switch
        turn to the other player. If the coordinate is already taken by either
        player, or an invalid coordinate (nothing will be flipped if the player
        place the piece here), then it will do nothing and the turn remains the same
        """
        if (col not in range(self._NUMBER_OF_COLUMNS)) or (row not in range(self._NUMBER_OF_ROWS)):
            raise OthelloIndexError
        result = drop_that_piece(col, row, self._NUMBER_OF_COLUMNS, self._NUMBER_OF_ROWS, self._board, self._turn)
        if len(result) == 0:
            pass
        else:
            self._board[col][row] = "{:3}".format(self._turn)
            for i in result:
                self._board[i[0]][i[1]] = "{:3}".format(self._turn)
            self._turn = _opposite_turn(self._turn)
        
    def countpieces(self) -> "how many pieces each player has":
        """
        Returns the count of each player's pieces on the board
        """
        [black, white] = [0, 0]
        for col in self._board:
            for item in col:
                if item.strip() == BLACK: black += 1
                elif item.strip() == WHITE: white += 1
        return "Black: {} -- White: {}".format(black, white)
    
def drop_that_piece(col: "y-coordinate", row: "x-coordinate",
                    COLUMNS: int, ROWS: int, board: [list], turn: str) -> list:
    """
    Returns a list of coordinations of the pieces should be flipped. This function
    will check 8 directions whenever a piece is dropped. It returns an empty list
    if the there is no piece that needs to be flipped, or the spot isn't empty
    """
    result = []
    while True:
        if board[col][row].strip() == EMPTY: pass
        else: break
        for direction_col,direction_row in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]:
            if not _on_board(col, row, COLUMNS, ROWS): break
            [y ,x] = [col,row]
            [y, x] = [y+direction_col, x+direction_row]
            if not _on_board(y, x, COLUMNS, ROWS): continue
            while board[y][x].strip() == _opposite_turn(turn):
                [y, x] = [y+direction_col, x+direction_row]
                if not _on_board(y, x, COLUMNS, ROWS): break
                if board[y][x].strip() == turn:
                    while True:
                        [y, x] = [y-direction_col, x-direction_row]
                        if y == col and x == row: break
                        result.append([y,x])
                    break
        break
    return result
        
def set_up(board: [list], rows: int, columns: int) -> None:
    """
    Displays the board and prints out the numbers of rows/columns
    """
    print(_displaying_columns(columns))
    for index1 in range(rows):
        for index2 in range(columns):
            print(board[index2][index1], end = "")
        print(str(index1+1))

def _displaying_columns(columns: int) -> int:
    """
    Returns the number of columns in a formatted way
    """
    count = ""
    for num in range(columns):
        count += "{:3}".format(str(num+1))
    return count

def _new_game_board(columns: int, rows: int, topleft) -> [list]:
    """
    Returns a 2D list of the board. Promps the user to input whoever on top left
    """
    board = []
    top_left = topleft
    for col in range(columns):
        board.append([])
        for row in range(rows):
            board[-1].append("{:3}".format(EMPTY))
    if top_left == BLACK:
        color1 = BLACK
        color2 = WHITE
    elif top_left == WHITE:
        color1 = WHITE
        color2 = BLACK
    board[int(columns/2)-1][int(rows/2)-1] = "{:3}".format(color1)
    board[int(columns/2)][int(rows/2)] = "{:3}".format(color1)
    board[int(columns/2)][int(rows/2)-1] = "{:3}".format(color2)
    board[int(columns/2)-1][int(rows/2)] = "{:3}".format(color2)
    return board

def _opposite_turn(turn: str) -> str:
    """
    Returns the opposite turn
    """
    if turn == BLACK: return WHITE
    else: return BLACK

def _on_board(y: "coordinate", x: "coordinate", columns: int, rows: int) -> bool:
    """
    Returns a boolean expression to check if the piece is on the board or not
    """
    return y < columns and y >= 0 and x < rows and x >= 0

def _check_every_piece(COLUMNS: int, ROWS: int, board: [list], turn: str) -> list:
    """
    Check every possible move a player can make (if there is no possible move,
    the turn will be switched to the other player, but it won't be executed in
    this function)
    """
    result = []
    answer = []
    for col in range(COLUMNS):
        for row in range(ROWS):
            checking = drop_that_piece(col, row, COLUMNS, ROWS, board, turn)
            result.append(checking)
    for moves in result:
        answer.extend(moves)
    return answer


        
            
            
