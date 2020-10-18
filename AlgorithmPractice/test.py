import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np

mpl.style.use('classic')

sal = pd.read_csv("C:/Users/doubl/PyDataScience/04-Pandas-Exercises/Salaries.csv")
print(sal.info())

sns.barplot(x='Year', y='BasePay', data=sal)

plt.show()