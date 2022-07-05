#the problem is that even with pyxlsb, if a file is created without a cache (i think)
#you won't be able to use that data in a dataframe from pandas
#this happens not just because there are formulas, but also when a file is created thru ms access w/transferspreadsheet

import win32com.client 
import sys
import pandas
import time

from pyxlsb import open_workbook   

uploadLoc = 'path/to/ur/location.xlsb'

excel = win32com.client.gencache.EnsureDispatch('Excel.Application')
excel.DisplayAlerts = False # disabling prompts to overwrite existing file
excel.Workbooks.Open(uploadLoc)
#need this or it tries to save right away and you have issues
time.sleep(16)
excel.ActiveWorkbook.Save()
excel.DisplayAlerts = True # enabling prompts
excel.ActiveWorkbook.Close()

with open_workbook(uploadLoc)  as wb:
    with wb.get_sheet(1) as sheet:
        for row in sheet.rows():
            df.append([item.v for item in row])

urDictionary = pandas.DataFrame(df[1:],columns=df[0])
print(urDictionary) #should work, here's test
