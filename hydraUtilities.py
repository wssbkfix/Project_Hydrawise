'''
Read and write for Hydrawise Schedle or 
Usage Report 
Steps
1 - Read config file and set variables  
2- read Excel input file 
3 - verify the type 
4 - write the output sheet
'''

import openpyxl as opxl 
import sys 
from datetime import datetime 
import readExcelWorkbook as readxls
import readConfigFile as cfg  
from writeSpreadSheet import writeSpreadSheet
import  DateUtils as dtUtils 

## get sheet attributes to determine type and sheets 
global configList 

def ReadAndWriteReport(inputSheet, spreadsheetName):
    ## 1 - read config report 
    global configList
    configList = cfg.readConfigFile("List")
    Path = configList["Path"]
       
        ## 2 - read Excel input file 
    inputSheet  = Path + inputSheet
    results   = readxls.readExcelWorkbook(inputSheet)
    roseList = results[0]
    schrubList = results[1]
    treeList = results[2]


    
    ## get the type 
    sheetType = readxls.getSheetType(inputSheet)  
    
    ## 3 - verify the type 
    if sheetType == 'SCH':
        sheetName = configList["OutputSchedule"]
    elif sheetType == 'USG' :
        sheetName = configList["OutputUsage"]
    else: 
        sheetName = ' '
    ## 4 - write the output sheet 
    if sheetName > ' ' : 
        writeSpreadSheet(spreadsheetName,sheetName,roseList, 'Rose')
        writeSpreadSheet(spreadsheetName,sheetName,schrubList, 'Schrub')
        writeSpreadSheet(spreadsheetName,sheetName,treeList, 'Tree')

def ReadAndWriteBridge(inputSheet):
    ## 1 - read config report 
    configList = cfg.readConfigFile("Bridge")
    NewSS = configList["NewSS"]
    Test  = configList["Test"]
    if Test == 'Y' : 
       NewSS = NewSS + '_tst'
    
    Path = configList["Path"]
          
        ## 2 - read Excel input file 
    inputSheet  = Path + inputSheet
    results = '' 
    results   = readxls.readExcelWorkbook(inputSheet)
    lista = results[0]
    sheetType  = results[1]
    hdrRow =     results[2]
    
    ##resultsC =  bulldCurrent(lista,YearMonth) 
    ##resultsP =  bulldPrevious(lista,YearMonth)
    
    ## 3 - verify the type 
    if sheetType == 'SCH':
        sheetNameC = "WaterSchC"
        sheetNameP = "WaterSchP"
    elif sheetType == 'USG' :
        sheetNameC = "WaterUsgC"
        sheetNameP = "WaterUsgP"
    else: 
        sheetName = ' '
    
    ## 4 - write the output sheet 
    if str(sheetType) == 'SCH' : 
     writeSpreadSheet(NewSS,'WaterSch',lista,"",hdrRow)
    if str(sheetType) == 'USG': 
     writeSpreadSheet(NewSS,'WaterUsg',lista,"",hdrRow)



def MergeAndSort(lista,listb,yearMonth):    
   mergedAndSorted = sorted(lista + listb, key=lambda x: (x[0], x[1], x[2]))
   ##filter out unwatned month 
   month = int(yearMonth[6:])
   outArray = []
   for row in mergedAndSorted:
    monthArry = int(row[1].month) 
    if monthArry == month:
        outArray.append(row)
   
   return outArray

def detSchUsgSheet(SchUsgSw):
    if SchUsgSw == 'S':
      return  'WaterSch'
    else:
      return 'WaterUsg'
    
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

def getDateParms():
   global configList
   yearMonth = configList["YearMonth"]
   startDay =  configList["StartDay"]
   endDay   =  configList["EndDay"]

   month = yearMonth[5:7]
   return [month, startDay,endDay]