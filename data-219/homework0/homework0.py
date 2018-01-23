import pandas as pd
import matplotlib.pyplot as plt

poke_species = pd.read_csv("pokemon_species.csv",index_col=1)
poke_species = poke_species.fillna(0)
hatch_time = poke_species.hatch_counter
hatch_time_hist = hatch_time.plot(kind='hist', bins=18, title='Pokemon Gestation Time')
hatch_time_hist.set_xlabel("Hatching Time (egg cycles)")
hatch_time_hist.set_ylabel("Hatching Time Frequency")
plt.close()

catch_rate = poke_species.capture_rate
catch_rate_hist = catch_rate.plot(kind='hist', bins=13, title='Pokemon Capture Rate')
catch_rate_hist.set_xlabel("Capture Rate")
catch_rate_hist.set_ylabel("Capture Rate Frequency")
plt.close()

plt.scatter(hatch_time, catch_rate)
plt.title('Pokemon Gestation Time and Capture Rate')
plt.xlabel("Gestation Time")
plt.ylabel("Capture Rate")
plt.close()

dresses_excel = pd.ExcelFile("Attribute DataSet.xlsx")
dresses = dresses_excel.parse("Sheet1")
dresses.Season = dresses.Season.str.title()
dresses.SleeveLength = dresses.SleeveLength.str.lower()
dresses.Price = dresses.Price.str.title()
dresses.Style = dresses.Style.str.lower()

dresses = dresses.replace("capsleeves","cap-sleeves")
dresses = dresses.replace("halfsleeve","half")
dresses = dresses.replace("sleeevless","sleeveless")
dresses = dresses.replace("sleevless","sleeveless")
dresses = dresses.replace("slevless","sleeveless")
dresses = dresses.replace("sleveless","sleeveless")
dresses = dresses.replace("threequater","threequarter")
dresses = dresses.replace("threequatar","threequarter")
dresses = dresses.replace("thressqatar","threequarter")
dresses = dresses.replace("turndowncollor","turndowncollar")
dresses = dresses.replace("urndowncollor","turndowncollar")
dresses = dresses. replace("Automn","Autumn")

dresses.groupby("SleeveLength").Season.value_counts()

top_styles = dresses.Style.value_counts().iloc[0:10]
top_styles.plot(kind="bar", title="Ten Most Common Dress Styles")
plt.xlabel("Dress Styles")
plt.ylabel("Frequency of Dress Style")
plt.tight_layout()
plt.close()

price_by_rating = dresses[["Price","Rating"]]
price_by_rating.boxplot(by="Price")
plt.title("Clothing Price Range vs Rating")
plt.xlabel("Price Range")
plt.ylabel("Rating")
plt.suptitle("")
plt.close()

personality_scores = pd.read_csv("data.csv")
personality_scores.gender = personality_scores.gender.replace(1,"male")
personality_scores.gender = personality_scores.gender.replace(2,"female")
scores_by_gender = personality_scores[["gender","score"]]
scores_by_gender = scores_by_gender[(scores_by_gender.gender == "female") | (scores_by_gender.gender == "male")]
scores_by_gender.boxplot(by="gender",notch=True)
plt.title("Narcissism Score Based On Gender")
plt.xlabel("Gender")
plt.ylabel("Score")
plt.suptitle("")
plt.close()

age_errors = personality_scores[(personality_scores.age > 100) | (personality_scores.age < 14)].index
purged_scores = personality_scores
purged_scores.age = purged_scores.age.drop(age_errors)

plt.scatter(purged_scores.age,purged_scores.score,s=5)
plt.title("Narcissism Score and Age")
plt.xlabel("Age")
plt.ylabel("Score")
plt.close()

time_errors = personality_scores[personality_scores.elapse > 1200].index
purged_scores.elapse = purged_scores.elapse.drop(time_errors)
purged_scores.elapse = purged_scores.elapse / 60
plt.scatter(purged_scores.score,purged_scores.elapse,s=5)
plt.title("Narcissism Score and Time Taken")
plt.xlabel("Score")
plt.ylabel("Time (mins)")
plt.close()