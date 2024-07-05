import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, chi2
from scipy.stats import f as fisher

# Parâmetros iniciais
mean1 = 50
mean2 = 70
variance = 10
std = np.sqrt(variance)
n1 = 100
n2 = 200
# n1 = 50
# n2 = 55
alpha = 0.05

# H0: As variâncias são iguais
# H1: As variâncias são diferentes
# É a probabilidade de falhar em rejeitar H0 quando H1 é verdadeira

# Gerando as amostras aleatórias independentes
sample1 = np.random.normal(loc=mean1, scale=std, size=n1)

# Desvios padrões ajustados
var1 = sample1.var()
r = 1.5
var2 = var1 * r

# sample2 = np.random.normal(loc=mean2, scale=std2, size=n2)

df1 = n1 - 1
df2 = n2 - 1

# Valores críticos de F para um teste bilateral
F_critical_lower = fisher.ppf(alpha/2, df1, df2)
F_critical_upper = fisher.ppf(1 - alpha/2, df1, df2)
print(F_critical_lower, F_critical_upper)

# Estatísticas F sob H1 (var2 > var1)
# var1 = std1**2
# var2 = std2**2
F = max(var2, var1) / min(var1, var2)

print(F, fisher.cdf(F, n2-1, n1-1))

# Calculando a probabilidade de erro tipo II (beta)
beta = 1 - fisher.cdf(F_critical_upper, n2-1, n1-1) + fisher.cdf(F_critical_lower, n2-1, n1-1)

print(f"Probabilidade de Erro Tipo II (beta) para r = {r}: {beta:.4f}")
print(1 - beta) # Checar quando dá 0.9

# Range de valores de F para plotagem
F_values = np.linspace(0.1, 5, 400)
pdf_H0 = fisher.pdf(F_values, df1, df2)
# pdf_H1 = fisher.pdf(F_values, df1, df2, loc=0, scale=F)

# Plot das distribuições
plt.figure(figsize=(10, 6))
plt.plot(F_values, pdf_H0, label='Distribuição F sob H0', color='blue')
# plt.plot(F_values, pdf_H1, label='Distribuição F sob H1 (r=1.5)', color='green')

# Pintando as regiões de não rejeição sob H0
plt.fill_between(F_values, pdf_H0, where=(F_values > F_critical_upper), color='red', alpha=0.5)
plt.fill_between(F_values, pdf_H0, where=(F_values < F_critical_lower), color='red', alpha=0.5, label='Região de não rejeição H0 sob H1')

# Linhas dos valores críticos
plt.axvline(x=F_critical_lower, color='black', linestyle='--', label='F crítico inferior')
plt.axvline(x=F_critical_upper, color='black', linestyle='--', label='F crítico superior')

plt.title('Distribuições F sob H0 e H1 com Áreas de Não Rejeição de H0')
plt.xlabel('Valores de F')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()
