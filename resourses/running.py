import pandas as pd
import glob
import os

# path = 'C:/Users/sewer/OneDrive/Рабочий стол/export-20200911-000/Sport-sessions'
# for filename in glob.glob(os.path.join(path, '*.json')):
# 	with open(os.path.join(os.getcwd(), filename), 'r') as f:
# 		print(f.read())

with open('json_info.json', 'r', encoding='utf-8') as json:
    