import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


    
iris = pd.read_csv(r"C:\Users\Owner\Desktop\UQ Year 3 Sem 2 Courses\STAT3006\Assignment 2\iris.csv")
iris = iris.drop(iris.iloc[:,0:1], axis = 1)
pairplot = sns.pairplot(iris, hue = "Species", markers=["o", "s", "D"])
pairplot.fig.suptitle("", y = 1.05)
iris.corr()


