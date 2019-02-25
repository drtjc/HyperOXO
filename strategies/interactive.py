import hypercube as hc
from strategy import Strategy

Cell_coord = hc.Cell_coord


class Interactive(Strategy):
    
    def __init__(self, d: int, n: int, moves_per_turn = 1, drop = False) -> None:
        super().__init__(d, n, moves_per_turn, drop)

    def move(self, cell: Cell_coord) -> Cell_coord:
        return (1,)

    def undo(self):
        pass