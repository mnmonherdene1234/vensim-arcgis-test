import pysd
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use("tkAgg")

model = pysd.load("./models/teacup.py")

temp = pd.Series(index=range(30), data=range(20, 80, 2))

stocks = model.run(progress=True, output_file="teacup_result.csv", params={
    'Room Temperature': 40
})

print(stocks["Teacup Temperature"])

print(type(stocks))

stocks["Teacup Temperature"].plot()
plt.title("Teacup Temperature")
plt.ylabel("Degrees F")
plt.xlabel("Minutes")
plt.grid()
plt.show()
