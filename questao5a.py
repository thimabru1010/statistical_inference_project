import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, chi2
from scipy.stats import f as fisher

# sample1 = np.random.normal(loc=mean1, scale=std, size=n1)
n1 = 100
n2 = 200

sample1 = np.random.normal(size=n1)
sample2 = np.random.normal(size=n2)

