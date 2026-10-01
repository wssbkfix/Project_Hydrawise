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
  OutSS              =    config["OutSS"]
  OutputSchedule     =  config["OutputSchedule"]
  OutputUsage        =  config["OutputUsage"]
  YearMonth          =  config["YearMonth"]
  StartDay           =  config['StartDay']
  EndDay             =  config['EndDay']
  Test               =  config["Test"]

   
  spreadsheetName  = OutSS + '_' + YearMonth 
  if Test =='Y':
    spreadsheetName += '_tst'

  HydraDict =  dict(
            Path = ["Folder Path", Path], 
            InputSchedule = ['Input Sch SS', InputSchedule],
            InputUsage = ['Input Usg SS ', InputUsage],
            OutSS = ['Out SS', OutSS],
            YearMonth = ['Year Month', YearMonth],
            Test = ['Test', Test],
            StartDay = ['Start Day', StartDay],
            EndDay = ['End Day', EndDay], 
            spreadsheetName = ['spreadsheet Name', spreadsheetName],
            OutputSchedule = ['Output Sch sheet', OutputSchedule],
            OutputUsage = ['Output Usg sheet', OutputUsage]
  ) 
    
    ##verify input files (spreadsheets) 
  InputSchedule = Path + InputSchedule 
  msg = excl.verfiyExcelWorkbook(InputSchedule)
  HydraDict['InputSchedule'].append(msg)

  InputUsage = Path + InputUsage 
  msg = excl.verfiyExcelWorkbook(InputUsage)
  HydraDict['InputUsage'].append(msg)

  try:
    gc = gspread.oauth()
    ssOut = gc.open(spreadsheetName)
    msg = 'found'
  except SpreadsheetNotFound:
    msg = 'Not found'
  HydraDict['spreadsheetName'].append(msg)


  ## verify output sheets 
  if msg == 'found':
    try:
      ssInWorksheet = ssOut.worksheet(OutputSchedule)
      msg = 'found'
    except WorksheetNotFound:
      msg = 'Not found'
    HydraDict['OutputSchedule'].append(msg)

    try:
      ssInWorksheet = ssOut.worksheet(OutputUsage)
      Msg= 'found'
    except WorksheetNotFound:
      Msg='Not foound'
    HydraDict['OutputUsage'].append(msg)
  

  return ssOut, HydraDict 
  

