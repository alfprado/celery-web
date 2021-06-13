import time
import pandas as pd

def create_file(content):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    df = pd.DataFrame(content)
    df.to_csv(f'{timestr}.csv',index=False)