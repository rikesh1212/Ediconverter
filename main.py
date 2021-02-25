import pandas as pd
from datetime import date, datetime

df = pd.read_excel("sample.xlsx")

today = date.today()
time =datetime.now()
d1= today.strftime("%m%d%Y")
d2 = time.strftime("%H%M")
data = [['ISA','00',' ','00',' ','079613350','ZZ','DMCOGDEN',d1,d2,'U','00305','222222222','1','T','>']]

df1 = pd.Data
