import json
import pandas as pd

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