##### This module makes sure the game keeps running until the user choose to exit

##### Execute this module to run the game

import OthelloModule
import OthelloGraphical
import OthelloGetInfo
import tkinter

def runOthello():
    """ Keeps the game running until the user choose to exit the program """
    while True:
        game = OthelloGraphical.OthelloGraphical(OthelloModule.Othello)
        if game.was_begin_clicked() == False: break
        if game.was_winning_clicked() == False: break
        game.start()
        if game.continue_option() == "Y": pass
        elif game.continue_option() == "N": break

        
        
if __name__ == "__main__":
    runOthello()
