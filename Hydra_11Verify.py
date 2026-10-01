'''
1 show configuration file   
## verfiies that everything has been setup.  
##  Verfiy the SS_ID points to the correct sheet
##
'''
  
##import json
import sys 
import verifyExcelWorkbook as excl
from displayComp import displayComp
from HydraVerifySub import HydraVerifySub
from GenUtilities import getAsList
from GenUtilities import insert_before_key

from tkinter import *

## initialize parent window 

ssOUt, HydraDict = HydraVerifySub("List")

HydraDict =  insert_before_key(HydraDict,'RevLin0',
                                    ['OS Files','-------------'],'Path')
HydraDict =  insert_before_key(HydraDict,'RevLin1',
                                  ['Spreadsheet Info','-------------'],'OutSS')
HydraDict =  insert_before_key(HydraDict,'RevLin2',
                                  ['Revised SS Name','-------------'],'spreadsheetName')

displayComp("1-Hydra Verify",HydraDict)

