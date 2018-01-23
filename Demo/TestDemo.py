#print('Hello World!')

#时间模块--datetime
#import time
#from datetime import date
#today = date.today()
#print(today)

#事件模块
import time
from datetime import date
today=date.today()
today.isoformat()
print(today.isoformat())
today.strftime("%d/%m/%y")

today.strftime("%d-%m-%y")

today.strftime("%A %d.%B %Y")