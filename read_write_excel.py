'''
说明：读取excel文件
'''

from xlrd import open_workbook
import csv,os
from path_file  import datapath

file_name=os.path.join(datapath,'test.xlsx')

class SheetypeError(Exception):
    pass

class ExcelRead_Write(object):
    '''读取excel文件'''

    def __init__(self,filename,sheet=0,title_line=True):
        if os.path.exists(filename):
            self.excel=filename
        else:
            raise FileNotFoundError('文件不存在！')

        self.sheet=sheet
        self.title_line=title_line
        self.data=[]

    def read(self):
        workbook=open_workbook(self.excel)
        if type(self.sheet) not in [int,str]:
            raise SheetypeError('Please pass in <type int> or <type str>,not {0}'.format(type(self.sheet)))
        elif type(self.sheet)==int:
            s=workbook.sheet_by_index(self.sheet)
        else:
            s=workbook.sheet_by_name(self.sheet)

        if self.title_line:
            title=s.row_values(0)
            for col in range(1,s.nrows):
                self.data.append(dict(zip(title,s.row_values(col))))

        else:
            for col in range(0,s.nrows):
                self.data.append(s.row_values(col))

        return self.data


reader=ExcelRead_Write(file_name).read()
print(reader)
