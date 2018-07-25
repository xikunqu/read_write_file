'''
说明：读取xml文件
'''

'''
xml文件格式如下：

<note>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note>
'''

from xml.dom import minidom
import os
from path_file  import datapath
file_name=os.path.join(datapath,'test.xml')

class XMLRead_Write(object):
    '''读取xml格式文件'''

    def __init__(self,filename):
        if os.path.exists(filename):
            self.xmlf=filename
        else:
            raise FileNotFoundError('文件不存在！')

    def read(self):
        self.data=minidom.parse(self.xmlf).documentElement
        to=self.data.getElementsByTagName('to')
        for i in range(len(to)):
            print(to[i].firstChild.data)
         #return self.data

xmlread=XMLRead_Write(file_name).read()