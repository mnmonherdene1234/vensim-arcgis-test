import pandas as pd

data = pd.read_csv("read_mdl_model.csv")

print(data.columns)

print(max(data["Teacup Temperature"]))
print(min(data["Teacup Temperature"]))
print(sum(data["Teacup Temperature"]))