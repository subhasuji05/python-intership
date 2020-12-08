import json
data=[{"name":"Siva","Age":"19","Place":"Madurai","Gender":"Male"},
      {"name":"Rio","Age":"31","Place":"Chennai","Gender":"Male"},
      {"name":"Bala","Age":"25","Place":"Chennai","Gender":"Male"},
      {"name":"Ramya","Age":"30","Place":"Chennai","Gender":"FeMale"}]

   with open("test.json",'w')as json_file:
    json.dump(data,json_file)

import pandas as pd
from sqlalchemy import create_engine
engine=create_engine('mysql+pymysql://root:@localhost/testintern')
df=pd.read_json("test.json")
df.to_sql("json_file",con=engine,if_exists='replace')