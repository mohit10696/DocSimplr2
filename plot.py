import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import csv

# with open('userdata.csv') as csvFile:
#     reader = csv.reader(csvFile)
#     field_names_list = next(reader)
#     field_names_list.pop(0)
#     #for i in field_names_list:


data = pd.read_csv("userdata.csv")
data.set_index("name", inplace=True)
#df2 = data.loc['17IT109']
data.plot.bar()
plt.savefig('abc.png',bbox_inches='tight')





