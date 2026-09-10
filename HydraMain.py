'''
1- read configList file and display results 
2- authenticate
3- Read and write Water schedule 
4- Read and write Water usage 

## ver 1.1 2 sheets at once efficent
## to do: clean up display 


'''

## test the hydrawise project see current capacity 
## current capacity 
##  Call the importHarawise Report to see if can read the excel file 

import sys 
import hydraUtilities as rdw 
import readExcelWorkbook  as readxls
import readConfigFile as cfg 
from writeSpreadSheet import writeSpreadSheet

from tkinter import *
import tkinter
from PIL import ImageTk,Image

from HydraVerifySub import HydraVerifySub

## initialize parent window 
root = Tk()
root.title("Hydra Main ")

## POsition the parent wndow using geomertry()
window_width = 500 
window_height = 400 

## get monitor dimensions 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate center-right X and Y Pixel coordinates 
center_x = int(screen_width/2)
center_y = int(screen_height/4)

## Apply format 
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")



## 1 Read and display Configlist values 
HydraVerifyArr = HydraVerifySub("List")


InputSchedule    =  HydraVerifyArr[2][1]
InputUsage       =  HydraVerifyArr[3][1]
spreadsheetName  = HydraVerifyArr[8][1]

rdw.ReadAndWriteReport(InputSchedule, spreadsheetName)
rdw.ReadAndWriteReport(InputUsage, spreadsheetName)


rowCount = 0 
for row in HydraVerifyArr:
    descValue = Label(root,text=row[0])
    value     = Label(root,text=row[1])
    descValue.grid(row=rowCount, padx=20, column=0,sticky=W)
    value.grid(row=rowCount, column=1,sticky=W)
    if len(row) == 3:
        descValue2 = Label(root,text=row[2])
        descValue2.grid(row=rowCount,column=2, sticky=W)

    rowCount += 1


root.mainloop()
