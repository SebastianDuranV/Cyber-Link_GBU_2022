class Votation():

    def __init__(self, name = "votación"):
        self.name = name
        self.yes = []
        self.no = []
        self.white = []

    def __str__(self):
        return "Yes: " + str(len(self.yes)) + " No: " + str(len(self.no)) + " White " + str(len(self.white))

    def addYes(self,idUser):
        self.yes.append(idUser)

    def addNo(self,idUser):
        self.no.append(idUser)

    def addWhite(self,idUser):
        self.white.append(idUser)

    def getStatus(self):
        return {"yes": len(self.yes), "no": len(self.no), "white": len(self.white)}