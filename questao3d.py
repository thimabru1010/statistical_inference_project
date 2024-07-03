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


# Calcular IC para cada sub-amostra
for i in range(num_samples):
    sample = samples[i]
    # print(sample)
    sample_mean = np.mean(sample)
    p_hat = sample_mean / 2
    
    # p ???
    se = np.sqrt(p*(1-p)/n) # std error, desvio padrao
    # print(p*(1-p))
    lower_bound = p_hat - z_value * se
    upper_bound = p_hat + z_value * se

    # Verificar se o IC contém o verdadeiro p
    if lower_bound <= p <= upper_bound:
        count_ic_contains_theta += 1

# Calcular o percentual de vezes que o IC contém o theta
percent_coverage = (count_ic_contains_theta / num_samples) * 100

print(f"O intervalo de confiança contém o parâmetro verdadeiro {percent_coverage}% das vezes.")

# intervalo de confiança = 10% das vezes

#! - d)

# Dados do experimento
p_0 = 0.95 
p_hat = percent_coverage / 100 
n = 100 

# Teste de hipótese
se = np.sqrt(p_0 * (1 - p_0) / n)
z = (p_hat - p_0) / se

# Valor crítico para um teste de duas caudas com alfa = 0.05
z_critical = norm.ppf(0.975)  # aproximadamente 1.96

# Decisão
print(f"Valor de Z: {z}")
print(f"Valor Crítico de Z: {z_critical}")
if abs(z) > z_critical:
    print("Rejeitar H0: A proporção observada é estatisticamente diferente de 0.95.")
else:
    print("Não rejeitar H0: A proporção observada não é estatisticamente diferente de 0.95.")

