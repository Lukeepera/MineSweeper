import pygame
import os

class Game:
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadimages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    def loadimages(self):
        self.images = {}

        for filename in os.listdir("Images"):
            if (not filename.endswith(".png")):
                continue
            image = pygame.image.load("Images/" + filename)

            image = pygame.transform.scale(image, self.pieceSize)
            self.images[filename.split(".")[0]] = image

    def getPiece(self, index):
        return self.board[index[0]], [index[1]]

    def getImage(self, piece):
        string = None

        return self.image[string]

        #gavcherdi 18;26 ze




