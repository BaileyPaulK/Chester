class Board:
    def __init__(self, id) -> None:
        self.id = id
        self.parts  = []    #note will be array of arrays [part object, qty used per board]
        self.flag = False   #True if stock issue
    
    def AddPart(self, part, qty):
        self.parts.append([part, qty])
 
    def IsMatch(self, testid):
        if self.id == testid:
            return True
        else:
            return False

    def Pull(self, qty):
        for part in self.parts:
            print("board: " + str(self.id) + " pulling " + str(part[0].id) + " qty: " + str((part[1] * qty)))
            part[0].Pull(part[1] * qty)
    
    def IsOut(self):
        for part in self.parts:
            if part[0].IsOut():
                self.flag = True
                print("BoardFlag: " + str(self.id))
        return self.flag