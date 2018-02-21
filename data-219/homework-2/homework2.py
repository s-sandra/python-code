import pandas as pd
import numpy as np

everything = pd.read_csv("activity.csv")
students = everything[["name","year","major","school","creds"]]
gpas = pd.melt(everything, ["name"], var_name="year", value_vars=["GPAFr","GPASo","GPAJr","GPASr"])

gpas = gpas.dropna()
gpas = gpas.replace("GPAFr","Fr")
gpas = gpas.replace("GPASo", "So")
gpas = gpas.replace("GPAJr", "Jr")
gpas = gpas.replace("GPASr", "Sr")
gpas = gpas.rename(columns = {"value":"GPA"})

schools = everything[["school","type","mascot"]]
del everything

schools["area"] = np.repeat("rural", len(schools))

# UVA, Richmond and UMW all urban.
urban_schools = np.where((schools.school == "UMW") | (schools.school == "Richmond") | (schools.school == "UVA"))
for school in urban_schools:
    schools.set_value(school, "area", "urban")
print(schools)