import openpyxl as opxl
from datetime import datetime
import hydraUtilities as utl 
import os 
import sys 
## open first sheet in workkbook

def readExcelWorkbook(path):

    try:
        wb = opxl.load_workbook(filename=path ) 
    except FileNotFoundError  as e: 
        print(f"file not found : {e} ")
        print("Please ensure the file is in the .xlsx format.")
        return
    except opxl as e:
        print("OPENPYXL error :  {e}")
    
       
    wsList = wb.sheetnames
   
    openSheet = wb.active 
    
    roseSheet =[]
    shrubsheet = []
    treeSheet = []

    dateArr = utl.getDateParms()
    month = dateArr[0]
    startDay = dateArr[1]
    endDay = dateArr[2]
    
    for wssheet in wsList:
        openSheet = wb[wssheet]
        wb.iso_dates = True
        for row in openSheet.iter_rows(values_only=False, min_row=1,min_col=1, max_col=4):
            i=0
            rowLine = []
            rowLine.append(wssheet)
            for cell in row:
                result = isinstance(cell.value,datetime)
                if isinstance(cell.value,datetime):
                    if i == 0:
                        rowLine.append(cell.value.strftime('%Y-%m-%d'))
                        i += 1
                    else: 
                        rowLine.append(cell.value.strftime('%H:%M:%S'))
                else:
                    rowLine.append(cell.value)

            lineMonth = rowLine[1][5:7]
            lineDay =   rowLine[1][8:10] 

            if lineMonth == month:
                if lineDay >= startDay and lineDay <= endDay:
                    if wssheet == 'Roses':
                        roseSheet.append(rowLine)
                    elif wssheet == 'Shrubs':
                        shrubsheet.append(rowLine)
                    elif wssheet == 'Trees':
                        treeSheet.append(rowLine)
            
    wb.close()  
    return [roseSheet, shrubsheet, treeSheet]


def getSheetType(sheetPath):
    fileName = os.path.basename(sheetPath)
    group = "_Sch"
    if group in fileName:
        return "SCH" 
    group = "SCH"
    if group in fileName:
        return "SCH" 
    group = 'Usg'
    if group in fileName:
        return "USG"
    group = 'USG'
    if group in fileName:
        return 'USG'

    return 'None'