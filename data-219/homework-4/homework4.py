# @author Sandra Shtabnaya

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
import numpy as np

api_key_1 = "blah"
api_key_2 = "blah"
rows = []
cities = ["D.C.", "San+Francisco", "Baltimore", "Portland", "Chicago", "Houston", "New+York+City", "Phoenix",
          "Las+Vegas", "Seattle"]
zips = ["20001", "94016", "97035", "21201", "60007", "77001", "10001", "85001", "88901", "98101"]

def get_stats(business, city):
    stats = []

    if "price" in business:
        price = business["price"]
        if price == "$":
            price = 1
        elif price == "$$":
            price = 2
        elif price == "$$$":
            price = 3
        else:
            price = 4
    else:
        price = np.nan

    city = city.replace("+", " ")
    name = business["name"].replace('""', '')
    id = business["id"]

    reviews = requests.get("https://api.yelp.com/v3/businesses/" + id + "/reviews",
                           headers={"Authorization": "Bearer " + api_key_1})
    reviews = json.loads(reviews.content)

    for review in reviews["reviews"]:
        rating = review["rating"]
        stats.append({"review": rating, "business": name, "city": city, "price": price})

    return stats


def get_response(business, city, offset):
    response = requests.get("https://api.yelp.com/v3/businesses/search?location=" + city + "&categories=" + business +
                            "&limit=50&radius=15000&offset=" + str(offset),
                            headers={"Authorization": "Bearer " + api_key_1})
    stats = json.loads(response.content)
    if stats["total"] <= 100:
        print("Not enough " + business + " for " + city)
    return json.loads(response.content)


plumbers = pd.read_csv("./plumbers.csv")

ax = sns.swarmplot(x="city", y="review", data=plumbers, color=".2", size=7, alpha=0.5)
for item in ax.get_xticklabels():
    item.set_rotation(45)

plt.show()
plt.close()

plumbers[["review", "city"]].boxplot(by="city", notch=True)
plt.title("Plumber Reviews by City")
plt.xlabel("City")
plt.ylabel("Review")
plt.suptitle("")
plt.xticks(rotation=90)
plt.show()
plt.close()


cleaners = pd.read_csv("./cleaners.csv")

ax = sns.swarmplot(x="city", y="review", data=cleaners, color=".2", size=7, alpha=0.5)
for item in ax.get_xticklabels():
    item.set_rotation(45)

plt.show()
plt.close()

cleaners[["review", "city"]].boxplot(by="city", notch=True)
plt.title("Carpet Cleaner Reviews by City")
plt.xlabel("City")
plt.ylabel("Review")
plt.suptitle("")
plt.xticks(rotation=90)
plt.show()
plt.close()
plt.close()