import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, chi2
from scipy.stats import f as fisher

# Parâmetros iniciais
mean1 = 50
mean2 = 70
variance = 10
std = np.sqrt(variance)
# n1 = 100
# n2 = 200
alpha = 0.05
power = 0.90
r = 1.5

std2 = std * r

# sample1 = np.random.normal(loc=mean1, scale=std, size=n1)
# sample2 = np.random.normal(loc=mean1, scale=std, size=n2)

# Valores críticos Z
Z_half_alpha = norm.ppf(1 - alpha/2)
print(Z_half_alpha)
Z_beta = norm.ppf(power)

# Cálculo do tamanho da amostra
# n = 2 * (Z_alpha + Z_beta)**2 / (np.log(r)**2)
# n = 2 * (Z_half_alpha + Z_beta)**2 / (np.log(r)**2)
# n = 2 * (Z_half_alpha + Z_beta) / (r**2)
# Cálculo do tamanho da amostra
# n = ((Z_half_alpha + Z_beta)**2 * (1 + r)**2) / (np.log(r)**2)
n = ((Z_half_alpha + Z_beta)**2) * variance*r / (variance*r - variance)


print(f"Tamanho da amostra: {int(n)}")

