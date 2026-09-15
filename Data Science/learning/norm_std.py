import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('student-math-5.csv')
scaler = MinMaxScaler()

df_norm = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
### Error???
print(df_norm)