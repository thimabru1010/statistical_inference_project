import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, chi2
from scipy.stats import f as fisher

# Parâmetros iniciais
mean1 = 50
mean2 = 70
variance = 10
# std = np.sqrt(variance)
# n1 = 100
# n2 = 200
alpha = 0.05
power = 0.90
r = 1.5

# Gerando as amostras aleatórias independentes
# sample1 = np.random.normal(loc=mean1, scale=std, size=n1)

# alpha = 0.05
# power = 0.90
# r = 1.5

# # Valores Z
# Z_alpha = norm.ppf(1 - alpha/2)
# Z_beta = norm.ppf(power)

# # Estimativas de variância (assumindo variância padrão s1^2 = 1 para simplificar)
# s1_squared = variance
# s2_squared = r * s1_squared

# # Cálculo do tamanho da amostra
# n = ((Z_alpha + Z_beta)**2 * (s1_squared + s2_squared)**2) / (s1_squared - s2_squared)**2

# print(f"Tamanho da amostra: {int(n)}")



# Parâmetros
alpha = 0.05
power = 0.90
r = 1.5  # Razão esperada das variâncias

# Valores críticos Z
Z_half_alpha = norm.ppf(1 - alpha/2)
Z_beta = norm.ppf(power)

# Cálculo do tamanho da amostra
# n = 2 * (Z_alpha + Z_beta)**2 / (np.log(r)**2)
n = 2 * (Z_half_alpha + Z_beta)**2 / (np.log(r)**2)

print(f"Tamanho da amostra: {int(n)}")

