import json
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt

# loads meterorite data into nasa_data object
data = open("meteorites.json", encoding="utf8")
nasa_data = json.load(data)

rows = []

# obtains only year and mass for each meteorite
for meteorite in nasa_data:

    if "year" in meteorite:
        date = meteorite["year"]

        if "mass" in meteorite:
            mass = meteorite["mass"]
            rows.append({"year" : date, "mass" : mass})

year_and_mass = pd.DataFrame(rows)

# parses only year from date, cast to int.
year_and_mass.year = year_and_mass.year.str[0:4]
year_and_mass.year = year_and_mass.year.astype(int)

# casts masses to float, converts from grams to pounds
year_and_mass.mass = year_and_mass.mass.astype(float)
year_and_mass.mass = round(year_and_mass.mass / 453.59237, 3)

# calculates and plots KDE for years, with bandwidth of 3
year_and_mass = year_and_mass.sort_values(by="year")
kde = scipy.stats.gaussian_kde(year_and_mass.year, bw_method = 3)
plt.plot(year_and_mass.year, kde(year_and_mass.year))
plt.title("Distribution of Meteorite Landing Years")
plt.xlabel("Year")
plt.ylabel("Probability Density")
plt.show()
plt.close()

# calculates and plots KDE for mass, with bandwidth of 3
year_and_mass = year_and_mass.sort_values(by="mass")
kde = scipy.stats.gaussian_kde(year_and_mass.mass, bw_method = 3)
plt.plot(year_and_mass.mass, kde(year_and_mass.mass))
plt.title("Distribution of Meteorite Mass")
plt.xlabel("Mass (lbs)")
plt.ylabel("Probability Density")
plt.show()
plt.close()