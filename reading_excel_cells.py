


#filename = r"D:\Users\703143501\Documents\GE Confidential\WIP\WFs\WF#173984409\1345430_890080_CostFile_Closeout.xlsx"
#sheetname = "Data Forming Tab"

## checking if the file exists

##flag = False
##if os.path.isfile(filename):
##    print("File exists")
##    flag = True
##else:
##    print("File not found")
##
##
##if flag:
##    workbook = xlrd.open_workbook(filename)
##    worksheet = workbook.sheet_by_name(sheetname)
##
##    #Cell to read J8
##    # A1 corresponds to 0, 0
##
##    row = 52
##    row = row - 1
##    column = 38
##    column = column - 1
##
##    value = worksheet.cell(row, column).value
##
##    print(value)
##    # $527,958
##    # AL52


import xlrd
import os
def closeout_value(filename, sheetname="Data Forming Tab", cell_location = (52, 38)):
    '''value at cell AL52 in the sheet Data Forming Tab'''
    if not os.path.isfile(filename):
        print("File not found")
        return None

    try:
        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_name(sheetname)
        row, column cell_location
        row = row - 1
        column = column - 1

        value = worksheet.cell(row, column).value

        return value

    except:
        print("Something went wrong!")
        return None



        
    
