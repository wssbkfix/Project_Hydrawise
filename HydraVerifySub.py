'''
1 show configuration file   
## verfiies that everything has been setup.  
##  Verfiy the SS_ID points to the correct sheet
##
'''
  

##import json
import sys 
import gspread 
from gspread.exceptions  import SpreadsheetNotFound 
from gspread.exceptions  import WorksheetNotFound 
import verifyExcelWorkbook as excl
import readConfigFile as cfg



## 1- verify configuration 

def HydraVerifySub(type):

  config = cfg.readConfigFile(type) 
  InputSchedule      =  config["InputSchedule"]
  InputUsage         =  config["InputUsage"]
  Path               =  config["Path"]
  NewSS            =    config["NewSS"]
  OutputSchedule     =  config["OutputSchedule"]
  OutputUsage        =  config["OutputUsage"]
  YearMonth          =  config["YearMonth"]
  Test               =  config["Test"]
  global spreadsheetName

  HydraVerifyArr = []
  HydraVerifyArr.append(["OS Files ", "--------------"])
  HydraVerifyArr.append(["Path  ", Path])
  HydraVerifyArr.append(["Input Schedule", InputSchedule])
  HydraVerifyArr.append(["Input Usage", InputUsage])
  HydraVerifyArr.append(["Spreadsheet Info ", "--------------"])
  HydraVerifyArr.append(["New SS", NewSS])
  HydraVerifyArr.append(["Year Month", YearMonth])
  HydraVerifyArr.append(["Revised FileName","------------"])
  spreadsheetName = NewSS + '_' + YearMonth
  if Test == 'Y':
    spreadsheetName = spreadsheetName + "_tst"
   
  HydraVerifyArr.append(["New SS", spreadsheetName])
  HydraVerifyArr.append(["SheetName Sch", OutputSchedule])
  HydraVerifyArr.append(["SheetName Usg", OutputUsage])
  HydraVerifyArr.append(["Test", Test])


  ##verify input files (spreadsheets) 
  InputSchedule = Path + InputSchedule 
  Msg = excl.verfiyExcelWorkbook(InputSchedule)
  HydraVerifyArr[2].append(Msg)

  InputUsage = Path + InputUsage 
  Msg = excl.verfiyExcelWorkbook(InputUsage)
  HydraVerifyArr[3].append(Msg)

  try:
    gc = gspread.oauth()
    ss = gc.open(spreadsheetName)
    Msg = 'found'
  except SpreadsheetNotFound:
    Msg = 'Not found'
  HydraVerifyArr[8].append(Msg)


  ## verify output sheets 
  if Msg == 'found':
    try:
      ssInWorksheet = ss.worksheet(OutputSchedule)
      Msg = 'found'
    except WorksheetNotFound:
      Msg = 'Not found'
    HydraVerifyArr[9].append(Msg)

    try:
      ssInWorksheet = ss.worksheet(OutputUsage)
      Msg= 'found'
    except WorksheetNotFound:
      Msg='Not foound'
    
    HydraVerifyArr[10].append(Msg)
    try:
        ssInWorksheet = ss.worksheet(OutputSchedule)
        Msg = 'found'
    except WorksheetNotFound:
        Msg = 'Not found'
    HydraVerifyArr[9].append(Msg)

    try:
      ssInWorksheet = ss.worksheet(OutputUsage)
      Msg= 'found'
    except WorksheetNotFound:
      Msg='Not foound'
      
    HydraVerifyArr[10].append(Msg)

  return HydraVerifyArr 

