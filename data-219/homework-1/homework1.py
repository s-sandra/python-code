# @author: sandra shtabnaya

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats.stats

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