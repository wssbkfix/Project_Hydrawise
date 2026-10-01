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
from   displayComp import displayComp
from GenUtilities import insert_before_key

from HydraVerifySub import HydraVerifySub


## 1 Read and display Configlist values 
ssOut, HydraDict = HydraVerifySub("List")

InputSchedule    =  HydraDict['InputSchedule'][1]
InputUsage       =  HydraDict['InputUsage'][1]
spreadsheetName  =  HydraDict['spreadsheetName'][1]

rdw.ReadAndWriteReport(ssOut, InputSchedule, spreadsheetName, HydraDict)
rdw.ReadAndWriteReport(ssOut, InputUsage, spreadsheetName, HydraDict)

HydraDict =  insert_before_key(HydraDict,'RevLin0',
                                    ['OS Files','-------------'],'Path')
HydraDict =  insert_before_key(HydraDict,'RevLin1',
                                  ['Spreadsheet Info','-------------'],'OutSS')
HydraDict =  insert_before_key(HydraDict,'RevLin2',
                                  ['Revised SS Name','-------------'],'spreadsheetName')

displayComp('2-Hydra Main', HydraDict)
