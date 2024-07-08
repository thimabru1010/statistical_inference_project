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
# n1 = n2 = 250
alpha = 0.05

# Parâmetros do teste
df1 = n1 - 1
df2 = n2 - 1
alpha = 0.05
ratio = 1.5

# Calculando valores críticos
F_critical_lower = fisher.ppf(alpha / 2, df1, df2)
F_critical_upper = fisher.ppf(1 - alpha / 2, df1, df2)

# Distribuições F sob H0 e Ha
F_dist_H0 = fisher(df1, df2)
F_dist_Ha = fisher(df1, df2, scale=ratio)

# Geração de valores de F para o gráfico
x = np.linspace(0.1, 5, 1000)
y_H0 = F_dist_H0.pdf(x)
y_Ha = F_dist_Ha.pdf(x)

beta = F_dist_Ha.cdf(F_critical_upper) - F_dist_Ha.cdf(F_critical_lower)
power = 1 - beta

print(f"Erro Tipo II (beta): {beta:.4f}")
print(f"Poder do teste (1-beta): {power:.4f}")

# Plotando as distribuições F sob H0 e Ha
fig = plt.figure(figsize=(10, 6))
plt.plot(x, y_H0, label='Distribuição F sob H0 (variâncias iguais)')
plt.plot(x, y_Ha, label='Distribuição F sob Ha (variância 1.5 vezes maior)')

# Área correspondente a beta sob Ha
x_fill_Ha = np.linspace(F_critical_lower, F_critical_upper, 1000)
y_fill_Ha = F_dist_Ha.pdf(x_fill_Ha)
plt.fill_between(x_fill_Ha, y_fill_Ha, color='gray', alpha=0.5, label='Beta (Erro Tipo II) sob Ha')

# Marcando os valores críticos
plt.axvline(F_critical_lower, color='red', linestyle='dashed', linewidth=2, label='Valor Crítico Inferior')
plt.axvline(F_critical_upper, color='red', linestyle='dashed', linewidth=2, label='Valor Crítico Superior')

# Adicionando detalhes ao gráfico
plt.title('Distribuições F sob H0 e Ha com área correspondente a Beta (Erro Tipo II)')
plt.xlabel('Estatística F')
plt.ylabel('Densidade')
plt.legend()
plt.grid(True)
plt.show()
fig.savefig('figures/erro_tipo2.png', dpi=300)

