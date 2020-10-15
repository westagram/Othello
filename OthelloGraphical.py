##### This module take in the game logic and turns it into a graphical user
##### interface. It will take whatever the user inputs in the other module
##### and create a game board out of it


import OthelloModule
import OthelloGetInfo
import tkinter

class OthelloGraphical:
    def __init__(self, state: "Othello game state"):
        """
        Initiates the whole game. Closes the program if the user chooses to exit
        the program
        """
        self._info = OthelloGetInfo.GettingInfo()
        
        self._info.show()
        
        if self._info.was_begin_click():
            
            self._winning_option = OthelloGetInfo.WinningOption()
            self._winning_option.show()
            if self._winning_option.was_winning_option_clicked():
                ##### Initiates the state, board, rows, columns, rows, turn,
                ##### winning option, and play again option
                self._state = state(self._info.get_columns(), self._info.get_rows(),
                                    self._info.get_turn(), self._info.get_top_left())
                self._board = self._state.listboard()
                self._rows = self._state.show_rows()
                self._columns = self._state.show_columns()
                self._turn = self._state.turn()
                self._option = self._winning_option.get_option()
                self._play_again_option = ""
                ##### Creates the root(game) window
                self._root_window = tkinter.Tk()
                [self._width, self._height] = [0,0]
                ##### Displays the score
                self._score = tkinter.StringVar()
                self._score.set(self._state.countpieces())
                self._score_window = tkinter.Label(self._root_window, textvariable = self._score)
                self._score_window.grid(row = 0, column = self._columns+1, rowspan = self._rows,
                                        sticky = tkinter.W)
                ##### Displays the turn
                if self._state.turn() == OthelloModule.BLACK: turn = "Black"
                elif self._state.turn() == OthelloModule.WHITE: turn = "White"
                self._turn = tkinter.StringVar()
                self._turn.set("Turn: {}".format(turn))
                self._turn_window = tkinter.Label(self._root_window, textvariable = self._turn)
                self._turn_window.grid(row = 1, column = self._columns+1, rowspan = self._rows,
                                       sticky = tkinter.W)
                ##### Creates canvases as the board
                for col in range(self._columns):
                    for row in range(self._rows):
                        self.create_canvas(col, row, '#ACFA58')
                        self._canvas.bind("<Button-1>", self._on_canvas_clicked)
                        self._canvas.bind("<Configure>", self._on_canvas_resized)
       
    def start(self) -> None:
        """
        Starts the window
        """
        self._root_window.mainloop()
    
    def was_begin_clicked(self) -> bool:
        """
        Returns whether or not the 'Begin!' button is clicked
        """
        return self._info.was_begin_click()

    def was_winning_clicked(self) -> bool:
        """
        Returns whether or not one of the winning options is clicked
        """
        return self._winning_option.was_winning_option_clicked()
    
    def destroy_window(self) -> None:
        """
        Destroys the window
        """
        self._root_window.destroy()

    def continue_option(self) -> str:
        """
        Returns whether of not the user wants to play another game
        """
        return self._play_again_option        

    def create_ovals(self) -> None:
        """
        Erases the canvas and redraws every piece
        """
        self._canvas.delete(tkinter.ALL)
        [self._height, self._width] = [self._canvas.winfo_width(), self._canvas.winfo_height()]
        for col in range(self._columns):
            for row in range(self._rows):
                self.create_oval(col, row)
        
    def create_canvas(self, col: int, row: int, color: str) -> None:
        """
        Creates a canvas without the pieces of the game. This will be the board
        """
        self._canvas = tkinter.Canvas(
            self._root_window, width = 50, height = 50, 
            borderwidth = 0,highlightthickness = 1,
            background = '#ACFA58', highlightbackground = 'black')
        self._canvas.grid(
            row = row, column = col, padx = 1, pady = 1,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        self._canvas.create_oval(0,0,self._height,self._width,
                                 fill = color, outline = color)
        self._root_window.rowconfigure(row, weight = 1)
        self._root_window.columnconfigure(col, weight = 1)
            
    def create_oval(self, col: int, row: int) -> None:
        """
        Creates an oval if the spot in the board isn't empty
        """
        if self._board[col][row].strip() == OthelloModule.BLACK:
            self.create_canvas(col, row, 'black')
        elif self._board[col][row].strip() == OthelloModule.WHITE:
            self.create_canvas(col, row, 'white')
        else: pass
                
    def display_score_turn(self) -> str:
        """
        Displays the current score and turn
        """
        self._score.set(self._state.countpieces())

        if self._state.turn() == OthelloModule.BLACK: turn = "Turn: Black"
        elif self._state.turn() == OthelloModule.WHITE: turn = "Turn: White"
        else: turn = "Game Over"
        self._turn.set(turn)


    def morepiecewin(self) -> "winner":
        """
        Returns the winner, whoever has more pieces on the board. If the score
        is tied, returns no winner
        """
        [black_count, white_count] = [0, 0]
        for item1 in self._board:
            for item2 in item1:
                if item2.strip() == OthelloModule.BLACK: black_count += 1
                elif item2.strip() == OthelloModule.WHITE: white_count += 1
        if black_count > white_count: winner = "BLACK"
        elif white_count > black_count: winner = "WHITE"
        elif black_count == white_count: winner = "no winner"
        return "The winner is: {}".format(winner)

    def lesspiecewin(self) -> "winner":
        """
        Returns the winner, whoever has less pieces on the board. If the score
        is tied, returns no winner
        """
        [black_count, white_count] = [0, 0]
        for item1 in self._board:
            for item2 in item1:
                if item2.strip() == OthelloModule.BLACK: black_count += 1
                elif item2.strip() == OthelloModule.WHITE: white_count += 1
        if black_count > white_count: winner = "WHITE"
        elif white_count > black_count: winner = "BLACK"
        elif black_count == white_count: winner = "no winner"
        return "The winner is: {}".format(winner)

    def _on_canvas_resized(self, event):
        """
        Calls on create_ovals() function if the canvas is configured
        """
        self.create_ovals()
        
    def _color_code(self) -> str:
        """
        Returns the color code (either 'black' or 'white') for the pieces
        """
        if self._state.turn() == OthelloModule.BLACK: return 'white'
        elif self._state.turn() == OthelloModule.WHITE: return 'black'

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        """
        Only if the board is clicked, then it will make a move. If it's an
        invalid move, it will do nothing. Once the game is over, it will pop
        up another Tk window and announce the winner
        """
        grid_info = event.widget.grid_info()
        self._state.drop(int(grid_info['column']), int(grid_info['row']))
        for col in range(self._columns):
            for row in range(self._rows):
                self.create_oval(col, row)
        self.display_score_turn()
        if self._state.turn() == OthelloModule.EMPTY:
            if self._option == "A": winner = self.morepiecewin()
            elif self._option == "B": winner = self.lesspiecewin()
            continue_option = OthelloGetInfo.Winner(winner)
            continue_option.show()
            self._play_again_option = continue_option.play_again_option()
            self._root_window.destroy()


