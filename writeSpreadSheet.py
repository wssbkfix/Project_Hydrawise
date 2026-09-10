import datetime
import os.path
import gspread
import sys 

#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import InstalledAppFlow
## modified to write to the hydrwise spreadshee for the moth 

## parameters
## entries list of list that are the spreadsheet entries 
## creds sign-in credentials 


##from googleapiclient.discovery import build
##from googleapiclient.errors import HttpError

# call to write spreadsheet entries 
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.

def writeSpreadSheet(ssName,sheetName, entries, t_type):

   gc = gspread.oauth()
   ss = gc.open(ssName)
   sheet = ss.worksheet(sheetName)

    
  ## assume header one row and is first row 
  ## by trans type 
   if sheetName == 'WaterSch':
      if t_type == 'Rose':
         namedRange = 'WaterSchRoseData'
      elif t_type == 'Schrub':
       namedRange = 'WaterSchSchrubData'
      elif t_type == 'Tree':
       namedRange = 'WaterSchTreeData'
   else:    ## assume usage 
      if t_type == 'Rose':
         namedRange = 'WaterUsgRoseData'
      elif t_type == 'Schrub':
         namedRange = 'WaterUsgSchrubData'
      elif t_type == 'Tree':
         namedRange = 'WaterUsgTreeData'

   ss.values_clear(namedRange)
   sheet.update(namedRange,entries)  
