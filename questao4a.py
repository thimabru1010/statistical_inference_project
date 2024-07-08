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
f_values = np.linspace(0.1, 3, 400)
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