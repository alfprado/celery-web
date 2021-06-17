import time
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'database.csv')
OUTPUT = os.path.join(BASE_DIR, 'output')

def create_file(id_task, content):
    timestr = time.strftime("%Y%m%d")
    df = pd.DataFrame(content)
    df.to_csv(f'{OUTPUT}/{id_task}-{timestr}.csv',index=False)

def read_db():
    data = []
    with open(DB_FILE, 'r')as f:
        for line in f.readlines():
            data.append(line.replace('\n', ''))
    return data