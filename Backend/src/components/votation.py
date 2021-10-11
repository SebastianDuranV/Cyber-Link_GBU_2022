class Votation():

    def __init__(self):
        self.yes = 0
        self.no = 0
        self.white = 0

    def __str__(self):
        return "Yes: " + str(self.yes) + " No: " + str(self.no) + " White " + str(self.white)

    def addYes(self):
        self.yes += 1

    def addNo(self):
        self.no += 1

    def addWhite(self):
        self.white += 1

    def getStatus(self):
        return {"yes": self.yes, "no": self.no, "white":self.white}