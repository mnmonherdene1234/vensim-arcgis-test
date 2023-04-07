import pysd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("tkAgg")

model = pysd.read_vensim("./models/teacup.mdl")

stocks = model.run(
    progress=True,
    output_file="read_mdl_model.csv",
)

stocks["Teacup Temperature"].plot()
plt.title("Teacup Temperature")
plt.ylabel("Degrees F")
plt.xlabel("Minutes")
plt.grid()
plt.show()
