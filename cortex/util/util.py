import time
import pandas as pd

def create_file(id_task, content):
    timestr = time.strftime("%Y%m%d")
    df = pd.DataFrame(content)
    df.to_csv(f'{id_task}-{timestr}.csv',index=False)

def read_db():
    data = []
    with open('db.txt', 'r')as f:
        for line in f.readlines():
            data.append(line.replace('\n', ''))
    return data