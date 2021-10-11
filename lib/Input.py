class Input:
    def __init__(self, boardName, qty, row, boards) -> None:
        self.qty = qty
        self.row = row
        self.flag = False   #True if stock issue
        for board in boards:
            if board.id == boardName:
                self.board = board
                break
    
    def Pull(self):
        print("Order " + str(self.board.id) + " qty: " + str(self.qty))
        self.board.Pull(self.qty)
    
    def IsOut(self):
        self.flag = self.board.IsOut()
        if self.flag:
            print("OrderFlag: " + str(self.board.id))
        return self.flag