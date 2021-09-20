from openpyxl import load_workbook
workbook = load_workbook(filename = "TestData.xlsx")
sheet = workbook.active

while True:
    cell = input("Please Input Cell: ")
    if cell == exit:
        break
    print(sheet[cell].value)
