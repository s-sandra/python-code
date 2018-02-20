import pandas as pd

everything = pd.read_csv("activity.csv")
students = everything[["name","year","major","school","creds"]]
gpas = pd.melt(everything, ["name"], var_name="year", value_vars=["GPAFr","GPASo","GPAJr","GPASr"])
gpas = gpas.dropna()
gpas = gpas.replace("GPAFr","Fr")
gpas = gpas.replace("GPASo", "So")
gpas = gpas.replace("GPAJr", "Jr")
gpas = gpas.replace("GPASr", "Sr")
schools = everything[["school","type","mascot"]]
print(gpas)