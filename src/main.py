# %%
import pandas as pd
import numpy as np
import os

# %%
PARENT_PATH = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
SOMETHING = os.path.join(PARENT_PATH, 'data', 'something.csv')
RESULTS = os.path.join(PARENT_PATH, 'results')

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
