class Board:
    def __init__(self, id) -> None:
        self.id = id
        self.parts  = []    #note will be array of arrays [part object, qty used per board]
    
    def AddPart(self, part, qty):
        self.parts.append([part, qty])
 