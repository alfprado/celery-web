import time
import pandas as pd

def create_file(id_task, content):
    timestr = time.strftime("%Y%m%d")
    df = pd.DataFrame(content)
    df.to_csv(f'{id_task}-{timestr}.csv',index=False)