'''
说明： 读取csv文件
'''
'''
csv文件格式如下：
name,password
张三,000000
李四,000000
'''

import csv,os
from path_file  import datapath

file_name=os.path.join(datapath,'test.csv')
file_name2=os.path.join(datapath,'write.csv')

class CSVRead_Write(object):
    '''CSV文件'''

    def __init__(self,filename):
        if os.path.exists(filename):
            self.csvfile=filename
        else:
            raise FileNotFoundError('文件不存在！')
        self.data=[]

    def readlist(self):
        with open(self.csvfile,encoding='utf-8',newline='') as f:
            f_csv=csv.reader(f)
            for line in f_csv:
                self.data.append(line)

        return self.data


    def readdict(self):
        with open(self.csvfile,encoding='utf-8',newline='') as f:
            f_csv=csv.DictReader(f)
            for line in f_csv:
                self.data.append(line)
        return self.data


csvread=CSVRead_Write(file_name).readdict()
print(csvread)
