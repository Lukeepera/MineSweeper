import pygame
from Modules.board import Board
import os
from Modules.solver import Solver
from time import sleep


class Game:
    def __init__(self, size, prob):
        self.images = {}
        self.board = Board(size, prob)
        pygame.init()
        self.sizeScreen = self.calculate_screen_size(size)
        self.screen = pygame.display.set_mode(self.sizeScreen)
        self.pieceSize = (self.sizeScreen[0] // size[1], self.sizeScreen[1] // size[0])
        self.loadPictures()
        self.solver = Solver(self.board)

    def calculate_screen_size(self, size):
        if size[0] == size[1]:
            return 1000, 1000
        else:
            cell_width, cell_height = 36, 36
            width = size[1] * cell_width
            height = size[0] * cell_height
            return width, height

    def loadPictures(self):
        imagesDirectory = "images"
        for fileName in os.listdir(imagesDirectory):
            if not fileName.endswith(".png"):
                continue
            path = os.path.join(imagesDirectory, fileName)
            img = pygame.image.load(path)
            img = img.convert()
            img = pygame.transform.scale(img, self.pieceSize)
            self.images[fileName.split(".")[0]] = img

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not (self.board.getWon() or self.board.getLost()):
                    rightClick = pygame.mouse.get_pressed(num_buttons=3)[2]
                    self.handleClick(pygame.mouse.get_pos(), rightClick)
                if event.type == pygame.KEYDOWN:
                    self.solver.move()
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
            if self.board.getWon():
                self.win()
                running = False
        pygame.quit()

    def draw(self):
        topLeft = (0, 0)
        for row in self.board.getBoard():
            for piece in row:
                rect = pygame.Rect(topLeft, self.pieceSize)
                image = self.images[self.getImageString(piece)]
                self.screen.blit(image, topLeft)
                topLeft = (topLeft[0] + self.pieceSize[0], topLeft[1])
            topLeft = (0, topLeft[1] + self.pieceSize[1])

    def getImageString(self, piece):
        if piece.getClicked():
            return str(piece.getNumAround()) if not piece.getHasBomb() else 'bomb-at-clicked-block'
        if self.board.getLost():
            if piece.getHasBomb():
                return 'unclicked-bomb'
            return 'wrong-flag' if piece.getFlagged() else 'empty-block'
        return 'flag' if piece.getFlagged() else 'empty-block'

    def handleClick(self, position, flag):
        index = tuple(int(pos // size) for pos, size in zip(position, self.pieceSize))[::-1]
        self.board.handleClick(self.board.getPiece(index), flag)

    @staticmethod
    def win():
        sound = pygame.mixer.Sound('sounds/win.wav')
        sound.play()
        sleep(3)
