import abc
from tictactoe import TicTacToe, Cell_coord
from typing import Tuple, Union, Optional


class Strategy(abc.ABC):

    @classmethod
    def validate(cls, d: int, n: int, moves_per_turn: int, drop: bool) -> bool:
        """ Are the supplied game paramters valid for the strategy? """
        return True

    def __init__(self, ttt: TicTacToe) -> None:
        super().__init__()
        self.ttt = ttt

    def reset(self) -> None:
        """ Play resets """
        self.ttt.reset()

    @abc.abstractmethod
    def move(self, cell: Optional[Cell_coord]) -> Union[Cell_coord, str]: 
        """ Calculate the move to be played """

    def undo(self):
        """ Undo last move played """
        self.ttt.undo()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Strategy:

            validate_found = False
            reset_found = False
            move_found = False
            undo_found = False
            for B in C.__mro__:
                for attr in B.__dict__:
                    if attr == "validate":
                        validate_found = True                    
                
                    if attr == "reset":
                        reset_found = True                    
                    
                    if attr == "move":
                        move_found = True
                    
                    if attr == "undo":                        
                        undo_found = True
                    
                    if validate_found and reset_found and move_found and undo_found:
                        return True

        return NotImplemented

