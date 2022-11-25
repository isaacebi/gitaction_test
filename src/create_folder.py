# %%
import pandas as pd
import numpy as np
import os

# %%
def folderA(parentPath):
    SOMETHING = os.path.join(parentPath, 'data', 'something.csv')
    RESULTS = os.path.join(parentPath, 'results')

    # %%
    isExist = os.path.exists(RESULTS)
    if not isExist:
        os.mkdir(RESULTS)

    # %%
    df = pd.read_csv(SOMETHING)

    for name in df.name:
        fileName = f"{name}.csv"
        filePath = os.path.join(RESULTS, fileName)
        with open(filePath, 'w'):
            pass

# %%
