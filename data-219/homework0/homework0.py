import pandas as pd
import matplotlib.pyplot as plt

poke_species = pd.read_csv("pokemon_species.csv",index_col=1)
poke_species = poke_species.fillna(0)
hatch_time = poke_species.hatch_counter
hatch_time_hist = hatch_time.plot(kind='hist', bins=20, title='Pokemon Gestation Time')
hatch_time_hist.set_xlabel("Hatching Time")
hatch_time_hist.set_ylabel("Hatching Time Frequency")

catch_rate = poke_species.capture_rate
catch_rate_hist = catch_rate.plot(kind='hist', bins=13, title='Pokemon Capture Rate')
catch_rate_hist.set_xlabel("Capture Rate")
catch_rate_hist.set_ylabel("Capture Rate Frequency")

plt.scatter(hatch_time, catch_rate)
plt.title('Pokemon Gestation Time and Capture Rate')
plt.xlabel("Gestation Time")
plt.ylabel("Capture Rate")
plt.close()

dresses_excel = pd.ExcelFile("Attribute DataSet.xlsx")
dresses = dresses_excel.parse("Sheet1")
#dresses.groupby("SleeveLength")