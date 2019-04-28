

import xlrd
import sys
class ExcelReader(object):
    xList = []
    yList = []
    ncol=0
    nrow=0

    def __init__(self):
        workbook = xlrd.open_workbook('Example.xlsx')
        worksheet = workbook.sheet_by_index(0)
        self.ncol = worksheet.ncols
        self.nrow = worksheet.nrows
        print(self.nrow-1)
        print("Excel")
        x=0
        for x in range(self.nrow-1):
              self.xList.append(int(worksheet.cell(x+1, 0).value))
              x+=1


        y=0
        for y in range(self.nrow-1):
            self.yList.append(int(worksheet.cell(y+1, 1).value))
            y+=1



    def get_Xlist(self):
        return self.xList


    def get_Ylist(self):
        return self.yList


    def get_Ncols(self):
        return self.ncol


    def get_Nrows(self):
        return  self.nrow