# %%
import pandas as pd
import numpy as np
import os

# %%
SOMETHING = os.path.join(os.getcwd(), 'data', 'something.csv')
RESULTS = os.path.join(os.getcwd(), 'results')

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
