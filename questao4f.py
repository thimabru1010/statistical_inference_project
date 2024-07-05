import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, chi2
from scipy.stats import f as fisher

# Parâmetros iniciais
mean1 = 50
mean2 = 70
variance = 10
std = np.sqrt(variance)
n1 = 55
# n2 = 200
n2 = n1
n = n1
alpha = 0.05
r = 1.5
power_0 = 0.9

# H0: As variâncias são iguais
# H1: As variâncias são diferentes
# É a probabilidade de falhar em rejeitar H0 quando H1 é verdadeira

# Gerando as amostras aleatórias independentes
# sample1 = np.random.normal(loc=mean1, scale=std, size=n1)
# sample2 = np.random.normal(loc=mean1, scale=std, size=n2)

# # Desvios padrões ajustados
# # std1 = sample1.std()
# # r = 1.5
# # std2 = sample2.std()

# # sample2 = np.random.normal(loc=mean2, scale=std2, size=n2)

# df1 = n1 - 1
# df2 = n2 - 1

# # Valores críticos de F para um teste bilateral
# F_critical_lower = fisher.ppf(alpha/2, df1, df2)
# F_critical_upper = fisher.ppf(1 - alpha/2, df1, df2)
# print(F_critical_lower, F_critical_upper)

# # Estatísticas F sob H1 (var2 > var1)
# var1 = sample1.var()
# var2 = sample2.var()
# F = max(var2, var1) / min(var1, var2)

# print(F, fisher.cdf(F, n2-1, n1-1))

# # Calculando a probabilidade de erro tipo II (beta)
# power = 1 - (1 - fisher.cdf(F_critical_upper, n2-1, n1-1) + fisher.cdf(F_critical_lower, n2-1, n1-1))
# r = var1 / var2

# print(f"Probabilidade de Erro Tipo II (beta) para r = {r}: {power:.4f}")

# Graus de liberdade
df1 = df2 = n - 1

# Valor crítico do teste F
f_critical = fisher.ppf(1 - alpha, df1, df2)

# Simular para estimar o poder
num_simulations = 10000
count = 0

# Valores críticos de F para um teste bilateral
F_critical_lower = fisher.ppf(alpha/2, df1, df2)
F_critical_upper = fisher.ppf(1 - alpha/2, df1, df2)

probs = []
for _ in range(num_simulations):
    # Gerar amostras com variâncias diferentes
    data1 = np.random.normal(0, variance, n) 
    data2 = np.random.normal(0, variance * r, n)  

    # Calcular variâncias amostrais
    var1 = np.var(data1)
    var2 = np.var(data2)
    
    # Calculando a probabilidade de erro tipo II (beta)
    # prob = 1 - (1 - fisher.cdf(F_critical_upper, n2-1, n1-1) + fisher.cdf(F_critical_lower, n2-1, n1-1))
    # probs.append(prob)
    # # Calcular a estatística F
    F = var1 / var2 if var1 > var2 else var2 / var1
    # if prob > power_0:
    #     count += 1
    # Contar quantas vezes rejeitamos H0
    if F > f_critical:
        count += 1

# Estimativa do poder
power = count / num_simulations

print("Estimado poder do teste:", power)
