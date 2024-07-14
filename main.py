from Modules.game import Game
from Modules.board import Board

size = (9, 9)
prob = 0.5
board= Board(size, prob)
screenSize= (1000, 1000)
game = Game(board, screenSize)
game.run()

