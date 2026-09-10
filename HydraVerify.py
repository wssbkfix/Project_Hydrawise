'''
1 show configuration file   
## verfiies that everything has been setup.  
##  Verfiy the SS_ID points to the correct sheet
##
'''
  
##import json
import sys 
import verifyExcelWorkbook as excl
from HydraVerifySub import HydraVerifySub

from tkinter import *

## initialize parent window 
root = Tk()
root.title("Hydra Verify")

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
## 1- verify configuration 

HydraVerifyArr = HydraVerifySub("List")

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

