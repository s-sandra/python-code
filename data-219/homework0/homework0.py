import pandas as pd
import matplotlib.pyplot as plt

poke_species = pd.read_csv("pokemon_species.csv",index_col=1)
poke_species = poke_species.fillna(0)
hatch_time = poke_species.hatch_counter
hatch_time_hist = hatch_time.plot(kind='hist', bins=20, title='Pokemon Gestation Time')
hatch_time_hist.set_xlabel("Hatching Time")
hatch_time_hist.set_ylabel("Hatching Time Frequency")
plt.show()