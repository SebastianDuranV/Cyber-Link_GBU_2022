class Votation():

    def __init__(self, name = "votación"):
        self.name = name
        self.yes = []
        self.no = []
        self.white = []

    def __str__(self):
        return "Yes: " + str(len(self.yes)) + " No: " + str(len(self.no)) + " White " + str(len(self.white))

    def addYes(self,idUser):
        if idUser in self.no:
            self.no.pop(idUser)
        
        if idUser in self.white:
            self.white.pop(idUser)

        self.yes.append(idUser)

    def addNo(self,idUser):

        if idUser in self.yes:
            self.yes.pop(idUser)
        
        if idUser in self.white:
            self.white.pop(idUser)

        self.no.append(idUser)

        

    def addWhite(self,idUser):
        if idUser in self.no:
            self.no.pop(idUser)
        
        if idUser in self.yes:
            self.yes.pop(idUser)

        self.white.append(idUser)

    def getStatus(self):
        return {"yes": len(self.yes), "no": len(self.no), "white": len(self.white)}