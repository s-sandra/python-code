# @author Sandra Shtabnaya and Nikki Lind

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.nonparametric.smoothers_lowess

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
del everything

# Sets UVA, Richmond and UMW area column to urban, all others to rural.
schools["area"] = np.where((schools.school == "UMW") | (schools.school == "Richmond") | (schools.school == "UVA"), "urban", "rural")

print("5. number of students: ", len(students))

senior_gpas = gpas[gpas.year == "Sr"]

print("6. number of end-of-year GPAs: ", len(gpas))
print("7. avg end-of-year gpa: ", gpas.GPA.mean())

students_and_schools = pd.merge(students, schools, on="school")
students_and_schools = students_and_schools.drop_duplicates()
print("8. Number of rural and urban students:\n", students_and_schools.area.value_counts())

students_by_area = students_and_schools[["name","area"]]
gpa_by_area = pd.merge(students_by_area, gpas, on="name")
gpa_by_area = gpa_by_area[gpa_by_area.year == "Fr"] # only considers freshman gpas.
print("9. avg rural and urban freshman gpa:\n", gpa_by_area.groupby("area").GPA.mean())

freshman_vs_non_freshman = gpas
freshman_vs_non_freshman.year = np.where(gpas.year == "Fr", "Freshman", "Non-Freshman") # groups students into freshman vs non-freshman
freshman_vs_non_freshman.boxplot(by="year", notch=True)
print("10. There is a statistically significant difference between the average GPA of freshman and non-freshman.")
plt.title("Freshman vs Non-Freshman GPA")
plt.xlabel("Year")
plt.ylabel("GPA")
plt.suptitle("")
plt.show()
plt.close()

gpas_and_students = pd.merge(gpas, students, on="name")
print("11. There is a significant difference between the GPAs of certain majors. For example, CPSC versus ECON GPAs differ, as well as\n "
      "ECON versus ENGL. However, there is no significant difference between CPSC and ENGL GPAs")
gpas_and_students[["GPA", "major"]].boxplot(by="major", notch=True)
plt.title("End of Year GPA by Major")
plt.xlabel("Major")
plt.ylabel("GPA")
plt.suptitle("")
plt.show()
plt.close()

gpas_and_students[["GPA", "school"]].boxplot(by="school", notch=True)
print("12. There is a significant difference between the end-of-year GPAs of certain schools. For example, Richmond versus JMU GPAs differ\n"
      "as well as UVA versus VT. However, there is no significant difference between GPAs from CNU and JMU.")
plt.title("End of Year GPA by School")
plt.xlabel("School")
plt.ylabel("GPA")
plt.suptitle("")
plt.show()
plt.close()

gpa_and_creds = pd.merge(students, gpas, on="name")[["GPA", "creds"]]
gpa_and_creds.sort_values(by="creds")
plt.scatter(gpa_and_creds.creds, gpa_and_creds.GPA, s=2)
plt.title("End-of-Year GPA and Number of Credits")
plt.xlabel("Number of Credits")
plt.ylabel("GPA")

# plots loess line, with alpha of 1/4
lowess = statsmodels.nonparametric.smoothers_lowess.lowess(gpa_and_creds.GPA, gpa_and_creds.creds,frac=1/3)
plt.plot(lowess[:,0],lowess[:,1],color="red")
plt.show()