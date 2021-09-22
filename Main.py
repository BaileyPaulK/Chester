import os
from lib import DataLoad
from lib import Board
from lib import Part
boards = []
parts = []
for file in os.listdir("data"):#load data from all files in dir 
    if file.endswith(".xlsx"):
        print("Loading From: " + file)
        DataLoad.DataLoad(file, boards, parts)

#Load input
#calculate stock v qty
#output