import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros
k = 2
p = theta = 5
n = 200
num_samples = 100
z_value = 1.96  # Z-value para 95% de confiança

# Gerar amostras
np.random.seed(42)
samples = np.random.gamma(shape=k, scale=theta, size=(num_samples, n))

# Inicialização da contagem de ICs contendo o verdadeiro theta
count_ic_contains_theta = 0
# count_ic_contains_theta = []
        
lower_bounds = []
upper_bounds = []

# Calcular IC para cada sub-amostra para o máximo de observações (n = 200)
for j in range(1, n+1):
    sample_means = np.mean(samples[:, :j], axis=1)
    theta_hats = sample_means / 2
    # print(theta_hats)
    se = theta / (np.sqrt(2) * j)  # Erro padrão para o theta_hat ajustado para cada j
    #! erro padrao = desvio padrao / raiz de n
    
    lower_bound = np.mean(theta_hats - z_value * se)
    upper_bound = np.mean(theta_hats + z_value * se)
    
    # print(lower_bound, upper_bound)

    if lower_bound <= p <= upper_bound:
        count_ic_contains_theta += 1

    lower_bounds.append(lower_bound)
    upper_bounds.append(upper_bound)
    
# Calcular o percentual de vezes que o IC contém o theta
# print(count_ic_contains_theta)
percent_coverage = (count_ic_contains_theta / n) * 100

print(f"O intervalo de confiança contém o parâmetro verdadeiro {percent_coverage}% das vezes.")

# Plotar os resultados
fig = plt.figure(figsize=(10, 6))
plt.plot(range(1, n + 1), lower_bounds, label='Lower Bound do IC', color='green')
plt.plot(range(1, n + 1), upper_bounds, label='Upper Bound do IC', color='green')
plt.axhline(theta, color='red', linestyle='--', label='Valor Verdadeiro de Theta')

plt.xlabel('Número de observações (j)')
plt.ylabel('Valor de Theta e Limites do IC')
plt.title('Limites de Intervalo de Confiança e Valor Verdadeiro de Theta')
plt.legend()
plt.grid(True)
plt.show()
fig.savefig('figures/intervalo_confianca.png', dpi=300)

# Conforme o número de observações aumenta, o intervalo vai ficando menor, ou seja, mais confiante.

#! - d)

# Dados do experimento
alfa = 0.04
p_0 = 1 - alfa # Valor de alfa - Nível de significancia
p_hat = percent_coverage / 100
print("p_hat: ", p_hat)
n = 100 

# Teste de hipótese
se = np.sqrt(p_0 * (1 - p_0) / n)
z = (p_hat - p_0) / se

# Valor crítico para um teste de duas caudas com alfa = 0.05
z_critical = norm.ppf(1 - alfa/2)  # aproximadamente 1.96
print(norm.ppf(0.95) )

#H0: a proporção de intervalos de confiança que contém o valor de theta é igual da prevista 95% (nivel de confiança)
#H1: a proporção de intervalos de confiança que contém o valor de theta é diferente da prevista 95% (nivel de confiança)

# Decisão
print(f"\nValor de Z: {z}")
print(f"Valor Crítico de Z: {z_critical}")
if abs(z) > z_critical:
    print("Rejeitar H0")
else:
    print("Não rejeitar H0")

