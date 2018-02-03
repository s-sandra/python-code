# @author: sandra shtabnaya

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats.stats
import pandas as pd
import json

# length 10000, with mean of 3, standard deviation of .5, and song lengths below 0.5 and above 10 removed.
song_lengths = np.random.normal(3,.5,10000).clip(0.5,10)

# length 10000, with mean of 5 mil, standard deviation of 1 mil, and views below half a mil removed.
plays = np.random.normal(5000000,1000000,10000).clip(500000)

plt.scatter(song_lengths, plays,s=2)
# plt.show()
plt.close()

def printPearsonTest(data1, data2):
    pearson_test = scipy.stats.stats.pearsonr(data1, data2)
    return "Pearson coefficient: " + str(pearson_test[0]) + ", p-value: " + str(pearson_test[1])

print("Song length and plays:\n" + printPearsonTest(song_lengths, plays))

# length 5093, with mean of 45,000, standard deviation of 15,000, and salaries below 0, above 120,000 removed
salaries = np.random.normal(45000,15000,5093).clip(0,120000)

def calculateTax(salary):

    # tax bracket ranges
    ten_percent = 9325
    fifteen_percent = 37950 - 9326
    twenty_five_percent = 91900 - 37951
    twenty_eight_percent = 191650 - 91901
    tax = 0
    bracket_sum = 0

    if salary > ten_percent:
        bracket_sum += ten_percent
        tax += ten_percent * .10
    else:
        tax += (salary - bracket_sum) * .10
        return tax

    if salary > fifteen_percent:
        bracket_sum += fifteen_percent
        tax += fifteen_percent * .15
    else:
        tax += (salary - bracket_sum) * .15
        return tax

    if salary > twenty_five_percent:
        bracket_sum += twenty_five_percent
        tax += twenty_five_percent * .25
    else:
        tax += (salary - bracket_sum) * .25
        return tax

    if salary > twenty_eight_percent:
        tax += twenty_eight_percent * .28
    else:
        tax += (salary - bracket_sum) * .28
        return tax

    return tax

taxes = salaries.copy()
for salary in range(len(taxes)):
    taxes[salary] = calculateTax(taxes[salary])

plt.scatter(salaries, taxes,s=2)
# plt.show()
plt.close()

print("\nSalaries and taxes:\n" + printPearsonTest(salaries, taxes))

# length 1935, with mean of 50 mph, standard deviation of 20, with speeds below 0, above 100 removed
accident_speeds = np.random.normal(15,5,1935).clip(0,100)

# calculates slope of the line using (50 mph, $5000) and (10 mph, $500)
speeds = np.array([[50, 1],
                   [10, 1]])
costs = np.array([[5000]
                 , [500]])
solution = np.linalg.solve(speeds, costs)

damages = accident_speeds * solution[0] + solution[1] + np.random.normal(0,1000,1935)

plt.scatter(accident_speeds, damages, s=2)
# plt.show()
plt.close()
print("\nAccident speeds and damages:\n" + printPearsonTest(accident_speeds, damages))

# array of college students where 15% UMW, 38% JMU, 6% Richmond and 41% VATech
university = np.random.choice(["UMW", "JMU", "Richmond", "VATech"], size=8932, p=[.15,.38,.06,.41])

# array of college mascots perfectly correlated with university array.
mascot = np.where(university=="UMW","eagle", np.where(university=="JMU", "duke", np.where(university=="Richmond", "spider", "hokie")))

# array of college students' favorite foods, uncorrelated with university array.
fave_food = np.random.choice(["pizza","sushi","falafel"], size=8932, p=[.6,.1,.3])

# array of college student types, slightly correlated with university array.
student_type = np.where(university=="UMW", np.random.choice(["partier","scholar","rebel","dropout"], size=8932, p=[.10,.45,.10,.35]),
                np.where(university=="JMU", np.random.choice(["partier","scholar","rebel","dropout"], size=8932, p=[.40,.25,.15,.20]),
                np.where(university=="Richmond", np.random.choice(["partier","scholar","rebel","dropout"], size=8932, p=[.35,.35,.15,.15]),
                np.random.choice(["partier","scholar","rebel","dropout"], size=8932, p=[.30,.35,.15,.20]))))

print("\nUniversity and Mascot:")
print(pd.crosstab(university,mascot,margins=True))
print("\nchi2: ")
print(scipy.stats.chi2_contingency(pd.crosstab(university,mascot)))

print("\nUniversity and Favorite Food:")
print(pd.crosstab(university,fave_food,margins=True))
print("\nchi2: ")
print(scipy.stats.chi2_contingency(pd.crosstab(university,fave_food)))

print("\nUniversity and Student Type")
print(pd.crosstab(university,student_type,margins=True))
print("\nchi2: ")
print(scipy.stats.chi2_contingency(pd.crosstab(university,student_type)))

with open("views.json","r") as reports:
    CFPB_reports = json.load(reports)

print("\nCFPB report #4 description:")
print(CFPB_reports[3]["description"])

print("\nCFPB reports with at least 4000 view counts:")
for report in CFPB_reports:
    if report["viewCount"] >= 4000:
        print(report["name"])