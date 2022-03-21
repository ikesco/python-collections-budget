# Import The Expense Module
import collections
from itertools import count
# from nis import cat
from typing import Counter
import matplotlib.pyplot as plt
from . import Expense

# Read in the Spending data
expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)
# Convert the Dictionary to 2 Lists
spend_dict = zip(*top5)
category, count = spend_dict

fig, ax = plt.subplots()
ax.bar(category, count)
ax.set_title("# of Purchases by Category")
plt.show() 
        