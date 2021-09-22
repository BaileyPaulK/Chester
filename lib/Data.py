#class Data:    Not a viable solution because no nice logical way to create the parts/ boards in a generic scalable way
#    def __init__ (self, column) -> None:
#        self.column = column
#    
#    def load (self, value):
#        self.value = value
#
#
#from openpyxl import load_workbook
#def LoadExcel (file, data, parts, boards): #data is array of type Data
#    wb = load_workbook(filename = file)     #loads in workbook
#    sheet = wb.active                       #sets first sheet or tab as sheet
#    row = 2
#    while True:
#        for cell in data:
#            cell.value = sheet[cell.column + string(row)]
#        if data[0].value == 'None':
#            break
#        else:
#            for cell in data:

            

