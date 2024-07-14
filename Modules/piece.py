
class Piece:
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False


    def gethasBomb(self):
        return self.hasBomb


    def getclicked(self):
        return self.clicked


    def getflagged(self):
        return self.flagged

