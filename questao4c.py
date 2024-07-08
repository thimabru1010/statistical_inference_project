# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm, chi2
# from scipy.stats import f as fisher

# # Parâmetros das distribuições
# mean1 = 50  
# mean2 = 70
# variance = 10
# std = np.sqrt(variance)

# # Tamanhos das amostras
# n1 = 100
# n2 = 200

# # Gerando as amostras aleatórias independentes
# sample1 = np.random.normal(loc=mean1, scale=std, size=n1)
# sample2 = np.random.normal(loc=mean2, scale=std, size=n2)

# # H0: As variâncias são iguais
# # H1: As variâncias são diferentes

# var1 = sample1.var()
# var2 = sample2.var()

# # std1 = sample1.std()
# # std2 = sample2.std()

# lambda_ratio = var1 / var2

# lambdas = np.linspace(min(var1, var2), max(var1, var2), 100)
# f_values = []

# for lambda_ratio in lambdas:
#     var2_hat = var1 * lambda_ratio
#     sample2_mod = np.random.normal(mean2, var2_hat, n2)
#     var2 = sample2_mod.var()
#     # print(var2)
#     F_val = max(var1, var2) / min(var1, var2)
#     f_values.append(F_val)

# # Plotando a curva característica
# fig = plt.figure(figsize=(10, 6))
# plt.plot(lambdas, f_values, label='F-Statistic')
# plt.axhline(y=1, color='r', linestyle='--', label='F=1 (Variâncias Iguais)')
# plt.xlabel('Lambda (std_dev1 / std_dev2)')
# plt.ylabel('F-Statistic')
# plt.title('Curva Característica do Teste F vs. Lambda')
# plt.legend()
# plt.grid(True)
# plt.show()
# fig.savefig('figures/questao4c.png')

# '''
# Este código simula como a estatística F varia em resposta a diferentes razões de desvios padrão entre duas amostras, permitindo visualizar como mudanças na variância relativa influenciam o resultado do teste de igualdade de variâncias. A linha 
# 𝐹
# =
# 1
# F=1 marca o ponto onde as variâncias são consideradas iguais sob a hipótese nula. Valores de 
# 𝐹
# F acima ou abaixo de 1 indicam variâncias desiguais.

# Vamos executar este código para gerar as amostras, realizar o teste e plotar a curva.

# '''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, chi2
from scipy.stats import f as fisher


# Parâmetros das distribuições
mean1 = 50  
mean2 = 70
variance = 10
std = np.sqrt(variance)

# Tamanhos das amostras
n1 = 100
n2 = 200

# Gerando as amostras aleatórias independentes
sample1 = np.random.normal(loc=mean1, scale=std, size=n1)
sample2 = np.random.normal(loc=mean2, scale=std, size=n2)

# H0: As variâncias são iguais
# H1: As variâncias são diferentes

# Calcula as variâncias amostrais
var1 = sample1.var()
var2 = sample2.var()
print(var1, var2)

alpha = 0.05

# Estatistica de Teste
F_val = max(var1, var2) / min(var2, var1)

deg_freedom1 = n1 - 1
deg_freedom2 = n2 - 1

# F_critical_l = fisher.ppf(1-alpha/2, deg_freedom1, deg_freedom2)
F_critical_lower = fisher.ppf(alpha/2, deg_freedom1, deg_freedom2)
F_critical_upper = fisher.ppf(1-alpha/2, deg_freedom1, deg_freedom2)

print(F_val)
print(F_critical_lower, F_critical_upper)


# if F_val < F_critical_l or F_val > F_critical_r:
if F_val < F_critical_lower or F_val > F_critical_upper:
    print("Rejeitar H0: As variâncias são diferentes.")
else:
    print("Aceitar H0: As variâncias são iguais.")
    
# Gerar valores para a distribuição F
f_values = var1 / var2
# f_values = np.linspace(0.1, 3, 400)
f_pdf = fisher.pdf(f_values, deg_freedom1, deg_freedom2)


# Plotar a distribuição F
fig = plt.figure(figsize=(10, 6))
plt.plot(f_values, f_pdf, label='Distribuição F', color='blue')

# # Marcar o valor de F = 1.0
# plt.axvline(x=1.0, color='red', linestyle='--', label='F = 1.0')

# Marcar os valores críticos
plt.axvline(x=F_critical_lower, color='green', linestyle='--', label=f'F crítico inferior ({F_critical_lower:.2f})')
plt.axvline(x=F_critical_upper, color='purple', linestyle='--', label=f'F crítico superior ({F_critical_upper:.2f})')

plt.title('Distribuição F com graus de liberdade {} e {}'.format(deg_freedom1, deg_freedom2))
plt.xlabel('Valor de F')
plt.ylabel('Densidade de probabilidade')
plt.legend()
plt.grid(True)
plt.show()
fig.savefig('figures/distribuicao_f.png', dpi=300)