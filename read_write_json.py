'''
说明：读取json文件
'''

'''
json文件格式如下：
{
  "user": [
    { "name": "张三", "password": "000000"},
    { "name": "李四", "password": "000000"}
  ]
}

'''

import json,os
from path_file  import datapath

file_name=os.path.join(datapath,'test.json')

class JsonRead_Write(object):
    '''读取json格式文件'''

    def __init__(self,filename):
        if os.path.exists(filename):
            self.jsonf=filename
        else:
            raise FileNotFoundError('文件不存在！')

    def read(self):
        with open(self.jsonf,encoding='utf-8') as f:
            self.data=json.load(f)
        return self.data

jsonread=JsonRead_Write(file_name).read()
print(jsonread)
