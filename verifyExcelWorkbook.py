import openpyxl as opxl

def verfiyExcelWorkbook(workBookName):
  try:
      wb = opxl.load_workbook(filename=workBookName) 
      return "found"
  except FileNotFoundError  as e: 
      return 'Not found' 
  except opxl  as e:
      return 'Not found E' 

