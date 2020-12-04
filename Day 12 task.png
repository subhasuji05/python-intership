import json
data=[{"name":"Subha","Age":"19","Place":"Madurai","Gender":"Male"},
      {"name":"Suji","Age":"15","Place":"Chennai","Gender":"Male"},
      {"name":"Deepa","Age":"35","Place":"Chennai","Gender":"Female"},
      {"name":"Gopi","Age":"25","Place":"Chennai","Gender":"Male"}]

   with open("test.json",'w')as json_file:
    json.dump(data,json_file)

import pandas as pd
from sqlalchemy import create_engine
engine=create_engine('mysql+pymysql://root:@localhost/testintern')
df=pd.read_json("test.json")
df.to_sql("json_file",con=engine,if_exists='replace')