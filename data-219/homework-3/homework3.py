import json
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import statsmodels.nonparametric.smoothers_lowess

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

# calculates and plots KDE for years, with bandwidth of .8
year_and_mass = year_and_mass.sort_values(by="year")
kde = scipy.stats.gaussian_kde(year_and_mass.year, bw_method = .8)
plt.plot(year_and_mass.year, kde(year_and_mass.year))
plt.title("Distribution of Meteorite Landing Years")
plt.xlabel("Year")
plt.ylabel("Density Estimation")
plt.show()
plt.close()

# calculates and plots KDE for mass, with bandwidth of .2
year_and_mass = year_and_mass.sort_values(by="mass")
kde = scipy.stats.gaussian_kde(year_and_mass.mass, bw_method = .2)
plt.plot(year_and_mass.mass, kde(year_and_mass.mass))
plt.title("Distribution of Meteorite Mass")
plt.xlabel("Mass (lbs)")
plt.ylabel("Density Estimation")
plt.xlim(xmin=-100, xmax=1500)
plt.show()
plt.close()

# tests for exponential relationship between mass and frequency
plt.plot(year_and_mass.mass, kde(year_and_mass.mass))
plt.title("Distribution of Meteorite Mass")
plt.xlabel("Mass (lbs)")
plt.ylabel("Probability")
plt.yscale("log")
plt.show()
plt.close()

# creates semilog scatterplot for year vs. mass
plt.plot(year_and_mass.year, year_and_mass.mass, marker="o", linewidth=0, ms=1)
plt.yscale("log")
plt.title("Meteorite Mass Over Time")
plt.xlabel("Year")
plt.ylabel("Mass (lbs)")

# plots loess line, with alpha of 1/3
lowess = statsmodels.nonparametric.smoothers_lowess.lowess(year_and_mass.mass, year_and_mass.year, frac=1/10)
plt.plot(lowess[:,0],lowess[:,1],color="red")
plt.show()
plt.close()
year_and_mass_correlation = scipy.stats.stats.pearsonr(year_and_mass.year, year_and_mass.mass)

# creates semilog plot for years from 1750 - present vs. mass
year_and_mass = year_and_mass[year_and_mass.year > 1750]
plt.plot(year_and_mass.year, year_and_mass.mass, marker="o", linewidth=0, ms=1)
plt.yscale("log")
plt.title("Meteorite Mass Over Time")
plt.xlabel("Year")
plt.ylabel("Mass (lbs)")

# plots loess line, with alpha of 1/3
lowess = statsmodels.nonparametric.smoothers_lowess.lowess(year_and_mass.mass, year_and_mass.year, frac=1/3)
plt.plot(lowess[:,0],lowess[:,1],color="red")
plt.show()
plt.close()