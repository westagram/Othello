##### This module is in charge of all the tkinter window, except for the game
##### board itself. This module also prompt the user to input however they
##### want to arrange the board, or chose whether to play another game when
##### the game is over


import tkinter
import OthelloModule


class GettingInfo:
    def __init__(self):
        """
        Initiates a Tk window which includes the welcome line, instruction line,
        the 2 'Begin!' and 'Quit' buttons, and allows the user to input how the
        board will be initiate
        """
        self._color = "#FFD801"
        
        self._info_window = tkinter.Tk()

        canvas = tkinter.Canvas(
            master = self._info_window, width = 500, height = 400,
            background = self._color, highlightbackground = self._color)
        canvas.grid(
            row = 0, column = 0, rowspan = 9, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        ##### Creates a welcome line
        welcome = tkinter.StringVar()
        welcome.set("Welcome to Othello v2.0")
        welcome_text = tkinter.Label(
            master = self._info_window, textvariable = welcome,
            font = ('Forte', 40), background = self._color, highlightcolor = "white") 
        welcome_text.grid(
            row = 1, column = 0, columnspan = 1,
            sticky =tkinter.W)
        ##### Creates an instruction line
        instruction = tkinter.StringVar()
        instruction.set("Enter the following informations, then click 'Begin!' to play")
        instruction_text = tkinter.Label(
            master = self._info_window, textvariable = instruction,
            font = ('Script MT Bold', 20), background = self._color) 
        instruction_text.grid(
            row = 2, column = 0, columnspan = 1,
            sticky = tkinter.W)
        ##### Asks the user for the number of columns
        column_label = tkinter.Label(
            master = self._info_window, text = 'Number of columns (even number from 4-16):',
            font = ('Times New Roman', 20), background = self._color)
        column_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._column_entry = tkinter.Entry(
            master = self._info_window, width = 20, font = ('Ariel', 20))
        self._column_entry.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E + tkinter.N)
        ##### Asks the user for the number of rows
        row_label = tkinter.Label(
            master = self._info_window, text = 'Number of rows (even number from 4-16):',
            font = ('Times New Roman', 20), background = self._color)
        row_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._row_entry = tkinter.Entry(
            master = self._info_window, width = 20, font = ('Ariel', 20))
        self._row_entry.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E + tkinter.N)        
        ##### Asks the user to input which player will go first
        turn_label = tkinter.Label(
            master = self._info_window,
            text = "Who will make the first move ('black' or 'white'):",
            font = ('Times New Roman', 20), background = self._color)
        turn_label.grid(
            row = 6, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._turn_entry = tkinter.Entry(
            master = self._info_window, width = 20, font = ('Ariel', 20))
        self._turn_entry.grid(
            row = 6, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E + tkinter.N)        
        ##### Asks the user to input which player will be on top left
        top_left_label = tkinter.Label(
            master = self._info_window,
            text = "Who will be on the top left ('black' or 'white'):",
            font = ('Times New Roman', 20), background = self._color)
        top_left_label.grid(
            row = 7, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        self._top_left_entry = tkinter.Entry(
            master = self._info_window, width = 20, font = ('Ariel', 20))
        self._top_left_entry.grid(
            row = 7, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E + tkinter.N)
        ##### Creates a frame that includes the 'Begin!' and 'Quit' button
        button_frame = tkinter.Frame(master = self._info_window,
                                     background = self._color)
        button_frame.grid(
            row = 8, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
        ### Creates a 'Begin!' button
        begin_button = tkinter.Button(
            master = button_frame, text = 'Begin!', font = ('Times New Roman', 14),
            command = self._on_begin_button)
        begin_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        ### Creates a 'Quit' button
        quit_button = tkinter.Button(
            master = button_frame, text = 'Quit', font = ('Times New Roman', 14),
            command = self._on_quit_button)
        quit_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._info_window.rowconfigure(8, weight = 1)
        self._info_window.columnconfigure(1, weight = 1)

        self._begin_clicked = False
        self._columns = 1
        self._rows = 1
        self._turn = ""
        self._top_left = ""

    def show(self) -> None:
        """
        Waits for the window to finish running
        """
        self._info_window.grab_set()
        self._info_window.wait_window()

    def was_begin_click(self) -> bool:
        """
        Returns True if the 'Begin!' button is clicked and all the informations
        are inputted correctly
        """
        return self._begin_clicked
    
    def get_columns(self) -> int:
        """
        Returns the number of columns that the user inputs
        """
        return self._columns

    def get_rows(self) -> int:
        """
        Returns the number of rows that the user inputs
        """
        return self._rows

    def get_turn(self) -> str:
        """
        Returns who will go first, as the user inputs
        """
        if self._turn.lower() == "black": return OthelloModule.BLACK
        elif self._turn.lower() == "white": return OthelloModule.WHITE

    def get_top_left(self) -> str:
        """
        Returns who will be on top left, as the user inputs
        """
        if self._top_left.lower() == "black": return OthelloModule.BLACK
        elif self._top_left.lower() == "white": return OthelloModule.WHITE

    def _on_begin_button(self) -> None:
        """
        Destroys the Tk window if the the user inputs a correct format, else
        nothing will happen and another window will pop up if one of the
        inputs is incorrect
        """
        try: 
            self._columns = int(self._column_entry.get())
            self._rows = int(self._row_entry.get())
            self._turn = str(self._turn_entry.get()).strip()
            self._top_left = str(self._top_left_entry.get()).strip()

            if (self._columns <= 16 and self._columns >= 4 and self._columns%2 == 0
                and self._rows <= 16 and self._rows >= 4 and self._rows%2 == 0
                and (self._turn.lower() == "black" or self._turn.lower() == "white")
                and (self._top_left.lower() == "black" or self._top_left.lower() == "white")):
                self._begin_clicked = True
                self._info_window.destroy()
            else:
                invalid = InvalidWindow()
                invalid.show()
        except: pass
    
    def _on_quit_button(self) -> None:
        """
        Destroys the Tk window if the user click on the 'Quit' button
        """
        self._info_window.destroy()

class WinningOption:
    def __init__(self):
        """
        Initiates a (second) Tk window, which asks the user to select the winning
        option (the player with more or less pieces wins)
        """
        self._color = "#FFD801"

        self._option_window = tkinter.Tk()

        canvas = tkinter.Canvas(
            master = self._option_window, width = 300, height = 200,
            background = self._color, highlightbackground = self._color)
        canvas.grid(
            row = 0, column = 0, rowspan = 3, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        ##### Creates an instruction line
        option_label = tkinter.Label(
            master = self._option_window, text = "Please Select One Of The Following Winning Options:",
            font = ('Script MT Bold', 20), background = self._color)
        option_label.grid(
            row = 0, column = 0, padx = 100, pady = 10,
            sticky = tkinter.N + tkinter.E + tkinter.W)
        ##### Creates an options that allows the player with more pieces wins
        more_piece_win_button = tkinter.Button(
            master = self._option_window, text = "A: The Player With More Pieces Wins",
            font = ('Impact', 15), command = self._on_more_button_pressed)
        more_piece_win_button.grid(
            row = 1, column = 0, padx = 100, pady = 10,
            sticky = tkinter.S + tkinter.E + tkinter.W)
        ##### Creates an options that allows the player with less pieces wins
        more_less_win_button = tkinter.Button(
            master = self._option_window, text = "B: The Player With Less Pieces Wins",
            font = ('Impact', 15), command = self._on_less_button_pressed)
        more_less_win_button.grid(
            row = 2, column = 0, padx = 100, pady = 10,
            sticky = tkinter.N + tkinter.E + tkinter.W)

        self._option_window.rowconfigure(0, weight = 1)
        self._option_window.rowconfigure(1, weight = 1)
        self._option_window.rowconfigure(2, weight = 1)
        self._option_window.columnconfigure(0, weight = 1)

        self._option = ""
        self._winning_option_clicked = False

    def show(self) -> None:
        """
        Waits for the window to finish running
        """
        self._option_window.grab_set()
        self._option_window.wait_window()

    def was_winning_option_clicked(self) -> None:
        """
        Returns True if one of the winning options is clicked
        """
        return self._winning_option_clicked

    def get_option(self) -> str:
        """
        Returns the option that the user clicks
        """
        return self._option
    
    def _on_more_button_pressed(self) -> None:
        """
        Destroys the window if one of the button is clicked
        """
        self._winning_option_clicked = True
        self._option = "A"
        self._option_window.destroy()
        
    def _on_less_button_pressed(self) -> None:
        """
        Destroys the window if one of the button is clicked
        """
        self._winning_option_clicked = True
        self._option = "B"
        self._option_window.destroy()

class Winner:
    def __init__(self, winner: str):
        """
        Initiates the winner window, which lets the user knows who won the game
        and promp them the option to continue or quit
        """
        self._winner_window = tkinter.Tk()

        self._color = "#FA5858"
            
        canvas = tkinter.Canvas(
            master = self._winner_window, width = 500, height = 200,
            background = self._color, highlightbackground = self._color)
        canvas.grid(
            row = 0, column = 0, rowspan = 3, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        ##### Creates a label which lets the user know who won the game
        winner_label = tkinter.Label(
            master = self._winner_window, text = winner,
            font = ('Forte', 60), background = self._color)
        winner_label.grid(
            row = 0, column = 0, padx = 100, pady = 10, columnspan = 2,
            sticky = tkinter.N + tkinter.E + tkinter.W + tkinter.S)
        ##### Creates a 'PLAY AGAIN!' button, which allows the user to play again
        continue_button = tkinter.Button(
            master = self._winner_window, text = "PLAY AGAIN!",
            font = ('Times New Roman', 15), command = self._on_continue_button_pressed)
        continue_button.grid(
            row = 1, column = 0, padx = 50, pady = 10,
            sticky = tkinter.S + tkinter.E)
        ##### Creates a 'QUIT' button, which exits the program
        quit_button = tkinter.Button(
            master = self._winner_window, text = "QUIT",
            font = ('Times New Roman', 15), command = self._on_quit_button_pressed)
        
        quit_button.grid(
            row = 1, column = 1, padx = 50, pady = 10,
            sticky = tkinter.S + tkinter.W)

        self._winner_window.rowconfigure(0, weight = 1)
        self._winner_window.rowconfigure(1, weight = 1)
        self._winner_window.columnconfigure(0, weight = 1)
        self._winner_window.columnconfigure(1, weight = 1)

        self._option = ""

    def show(self) -> None:
        """
        Waits for the window to finish running
        """
        self._winner_window.grab_set()
        self._winner_window.wait_window()

    def play_again_option(self) -> str:
        """
        Returns the user's option to either play again or quit
        """
        return self._option
    
    def _on_continue_button_pressed(self) -> None:
        """
        Destroys the window if one of the options is clicked
        """
        self._option = "Y"
        self._winner_window.destroy()

    def _on_quit_button_pressed(self) -> None:
        """
        Destroys the window if one of the options is clicked
        """
        self._option = "N"
        self._winner_window.destroy()

class InvalidWindow():
    def __init__(self):
        """
        Initiates an invilid window, which pops up only when the user inputs
        a wrong information
        """
        self._invalid_window = tkinter.Tk()

        invalid_label = tkinter.Label(
            master = self._invalid_window,
            text = "One (or more) of the infomations is (are) incorrect!",
            font = ('Ariel', 20))
        invalid_label.grid(
            row = 0, column = 0, padx = 10, pady = 10, 
            sticky = tkinter.E + tkinter.W + tkinter.S)
        ##### Creates an '>>QUIT<<' button
        exit_button = tkinter.Button(
            master = self._invalid_window, text = ">>QUIT<<",
            font = ('Times New Roman', 15), command = self._on_exit_button_pressed)
        
        exit_button.grid(
            row = 1, column = 0,
            sticky = tkinter.N + tkinter.E + tkinter.W)

        self._invalid_window.rowconfigure(0, weight = 1)
        self._invalid_window.rowconfigure(1, weight = 1)
        self._invalid_window.columnconfigure(0, weight = 1)

    def show(self) -> None:
        """
        Waits for the window to finish running
        """
        self._invalid_window.grab_set()
        self._invalid_window.wait_window()

    def _on_exit_button_pressed(self) -> None:
        """
        Destroys the window if the quit button is clicked
        """
        self._invalid_window.destroy()



