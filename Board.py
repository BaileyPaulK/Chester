class Board:
    def __init__(self) -> None:
        self.parts  = []    #note will be array of arrays [part object, qty used per board]
    
    def AddPart(self, part, qty):
        self.parts.append([part, qty])
 