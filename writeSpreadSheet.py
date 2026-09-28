import gspread
import sys 
import hydraUtilities as utl 

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

def writeSpreadSheet(ssOut, sheetName, entries,t_type):

   sheet = ssOut.worksheet(sheetName)

   ## calculate range
   start =  utl.detLastRow(sheet,t_type) +1
   end = start + len(entries)-1
   
   if t_type == 'Rose':
      namedRange = 'A' + str(start) + ':E' + str(end) 
   elif t_type == 'Schrub':
      namedRange = 'G' + str(start) + ':K' + str(end) 
   elif t_type == 'Tree':
      namedRange = 'M' + str(start) + ':Q' + str(end)   

   ssOut.values_clear(namedRange)
   sheet.update(namedRange,entries)  
