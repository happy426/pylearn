import numpy as np
import pandas as pd


data = pd.DataFrame(np.arange(12).reshape(3, 4))
print(data)
data_T = pd.DataFrame(data.values.T)
print(data_T)


