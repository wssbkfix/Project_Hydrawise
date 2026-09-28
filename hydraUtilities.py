'''
Read and write for Hydrawise Schedle or 
Usage Report 
Steps
1 - Read config file and set variables  
2- read Excel input file 
3 - verify the type 
4 - write the output sheet
'''

import sys 
import readExcelWorkbook as readxls
import readConfigFile as cfg  
from writeSpreadSheet import writeSpreadSheet
import  DateUtils as dtUtils 

## get sheet attributes to determine type and sheets 


def ReadAndWriteReport(ssOut, inputSheet, spreadsheetName,HydraDict):
    ## 1 - read config report 
    
    ##configList = cfg.readConfigFile("List")
    Path = HydraDict['Path'][1]
     ## 2 - read Excel input file 
    results   = readxls.readExcelWorkbook(HydraDict, inputSheet)
    roseList = results[0]
    schrubList = results[1]
    treeList = results[2]
    
    ## get the type 
    sheetType = readxls.getSheetType(inputSheet)  
    
    ## 3 - verify the type 
    if sheetType == 'SCH':
        sheetName = HydraDict['OutputSchedule'][1]
    elif sheetType == 'USG' :
        sheetName = HydraDict['OutputUsage'][1]
    else: 
        sheetName = ' '
    ## 4 - write the output sheet 
    if sheetName > ' ' : 
        writeSpreadSheet(ssOut, sheetName,roseList, 'Rose')
        writeSpreadSheet(ssOut, sheetName,schrubList, 'Schrub')
        writeSpreadSheet(ssOut, sheetName,treeList, 'Tree')

def cvtCols(sheetValues):
   for row in sheetValues:
      row[1] = dtUtils.cvtToDate(row[1])
      row[2] = dtUtils.cvtToTime(row[2])
   return sheetValues
    
def cvtColsBack(sheetValues):
   for row in sheetValues:
      row[1] = dtUtils.cvtFrmDate(row[1])
      row[2] = dtUtils.cvtFrmTime(row[2])
   
   return sheetValues

def detLastRow(ss,t_type):
    if t_type == 'Rose':
          namedRange = 'A1:A100'
    elif t_type == 'Schrub':
          namedRange = 'G1:G100'  
    elif t_type == 'Tree':
          namedRange = 'M1:100'    

    sheetValues = ss.get(namedRange)

    lastRow = 0 
    for row in sheetValues:
        if row[0] <= ' ':
          break
        lastRow += 1 
    return lastRow
 
def detSchUsgSheet(SchUsgSw):
    if SchUsgSw == 'S':
      return  'WaterSch'
    else:
      return 'WaterUsg'

def removeDuplicates(sheetValuesIn):
    seenKeys = set() 
    uniqueData = []

    for row in sheetValuesIn:
    # Slice the first 3 elements and convert to a tuple key
        key = tuple(row[:3])
    
        if key not in seenKeys:
            seenKeys.add(key)
            uniqueData.append(row)
    return uniqueData 