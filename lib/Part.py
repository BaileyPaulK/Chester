class Part:
    def __init__(self, id, stock) -> None:
        self.id     = id            #unique part id
        self.stock  = int(stock)    #amount of part in stock
        self.qty    = int(0)        #counter used to keep track of total needed
        self.flag = False   #True if stock issue

    def Pull(self, qty):            #"pull" from stock
        self.qty += qty
        

    def IsOut(self):            #why are you reading this... pretty self explanitory... good code should comment it's self ya know... and yet you still read? why? do you think i'm going to say something funny? ... ... fine... 24
        if self.stock > self.qty:
            return False
        else:
            self.flag = True
            print("PartFlag: " + str(self.id))
            return True
            

    def IsMatch(self, testid):
        if self.id == testid:
            return True
        else:
            return False