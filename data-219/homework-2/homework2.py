import pandas as pd
import numpy as np

everything = pd.read_csv("activity.csv")
students = everything[["name","year","major","school","creds"]]
gpas = pd.melt(everything, ["name"], var_name="year", value_vars=["GPAFr","GPASo","GPAJr","GPASr"])

# reformats values for GPA and year columns
gpas = gpas.dropna()
gpas = gpas.rename(columns = {"value":"GPA"})
gpas.year = gpas.year.str[3:]

schools = everything[["school","type","mascot"]]
del everything

schools["area"] = np.repeat("rural", len(schools))

# UVA, Richmond and UMW all urban.
urban_schools = np.where((schools.school == "UMW") | (schools.school == "Richmond") | (schools.school == "UVA"))
for school in urban_schools:
    schools.set_value(school, "area", "urban")

# removes duplicated students
students = students.drop_duplicates(["name"])
print("number of students: ", len(students))

# removes duplicated gpas
gpas = gpas.drop_duplicates()
print("number of end-of-year GPAs: ", len(np.where(gpas.year == "Sr")[0]))
