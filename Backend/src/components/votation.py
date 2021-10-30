class Votation():

    def __init__(self, name = "votación"):
        self.name = name
        self.yes = []
        self.no = []
        self.white = []
        self.connected = []

    def __str__(self):
        return "Yes: " + str(len(self.yes)) + " No: " + str(len(self.no)) + " White " + str(len(self.white))

    def addYes(self,idUser):

        print("yes")
        if idUser in self.no:
            self.no.remove(idUser)
        
        if idUser in self.white:
            self.white.remove(idUser)

        self.yes.append(idUser)

    def addNo(self,idUser):

        if idUser in self.yes:
            self.yes.remove(idUser)
        
        if idUser in self.white:
            self.white.remove(idUser)

        self.no.append(idUser)

        

    def addWhite(self,idUser):
        if idUser in self.no:
            self.no.remove(idUser)
        
        if idUser in self.yes:
            self.yes.remove(idUser)

        self.white.append(idUser)

    def getStatus(self):
        conect = set(self.connected)
        return {"yes": len(self.yes), "no": len(self.no), "white": len(self.white), "connected": len(self.connected)}

    def connect(self,idUser):
        self.connected.append(idUser)

    def desconnect(self,idUser):
        self.connected.remove(idUser)
