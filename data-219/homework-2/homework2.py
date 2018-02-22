# @author Sandra Shtabnaya and Nikki Lind

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

everything = pd.read_csv("activity.csv")
students = everything[["name","year","major","school","creds"]]
gpas = pd.melt(everything, ["name"], var_name="year", value_vars=["GPAFr","GPASo","GPAJr","GPASr"])

# reformats values for GPA and year columns
gpas = gpas.dropna()
gpas = gpas.rename(columns = {"value":"GPA"})
gpas.year = gpas.year.str[3:] # chops off GPA in values of year column

# removes duplicated schools, adds area column
schools = everything[["school","type","mascot"]]
schools = schools.drop_duplicates()
schools["area"] = np.repeat("rural", len(schools))
del everything

# UVA, Richmond and UMW all urban.
urban_schools = np.where((schools.school == "UMW") | (schools.school == "Richmond") | (schools.school == "UVA"))
for school in urban_schools[0]:
    schools.set_value(school, "area", "urban")

# removes duplicated students
students = students.drop_duplicates(["name"])
print("5. number of students: ", len(students))

# removes duplicated gpas
gpas = gpas.drop_duplicates()
senior_gpas = np.where(gpas.year == "Sr")[0]
print("6. number of end-of-year GPAs: ", len(senior_gpas))

def calculateAvgGpa(gpas_list):
    sum_gpa = 0
    for gpa in gpas_list:
        sum_gpa += gpas.iloc[gpa].GPA
    return sum_gpa / len(gpas_list)

print("7. avg senior gpa: ", calculateAvgGpa(senior_gpas))

students_and_schools = pd.merge(students, schools, on="school")
students_and_schools = students_and_schools.drop_duplicates()
rural_students = np.where(students_and_schools.area == "rural")
urban_students = np.where(students_and_schools.area == "urban")
print("8. a) number of urban students: ", len(urban_students[0]))
print("8. b) number of rural students: ", len(rural_students[0]))

students_by_area = students_and_schools[["name","area"]]
gpa_by_area = pd.merge(students_by_area, gpas, on="name")
gpa_by_area = gpa_by_area[gpa_by_area.year == "Fr"] # only considers freshman gpas.

rural_gpa = np.where(gpa_by_area.area == "rural")
urban_gpa = np.where(gpa_by_area.area == "urban")
print("9. a) avg rural freshman gpa: ", calculateAvgGpa(rural_gpa[0]))
print("9. b) avg urban freshman gpa: ", calculateAvgGpa(urban_gpa[0]))

freshman_vs_non_freshman = gpas
freshman_vs_non_freshman.year = np.where(gpas.year == "Fr", "Freshman", "Non-Freshman")
freshman_vs_non_freshman.boxplot(by="year", notch=True)
plt.title("Freshman vs Non-Freshman GPA")
plt.xlabel("Year")
plt.ylabel("GPA")
plt.suptitle("")
plt.show()