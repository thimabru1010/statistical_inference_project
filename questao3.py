import numpy as np
import matplotlib.pyplot as plt

#! a)

# Definindo parâmetros da distribuição Gamma
k = 2
theta = 5
n = 200
num_samples = 100

# Gera 100 amostras, cada uma com n = 200 observações
samples = np.random.gamma(shape=k, scale=theta, size=(num_samples, n))

vies_empirico = []

# Calcula o estimador para cada sub-amostra e para cada j
for j in range(1, n):
    theta_hats = np.mean(samples[:, :j], axis=1) / 2  # média amostral / 2 para cada sub-amostra até j
    # print(theta_hats)
    vies = np.mean(theta_hats - theta)  # média dos desvios (estimadores - valor real)
    vies_empirico.append(vies)

# Gerar o gráfico do viés empírico
# fig = plt.figure(figsize=(10, 6))
# plt.plot(range(1, n + 1), vies_empirico, label='Viés Empírico de $\\hat{\\theta}_{i,j}$')
# plt.xlabel('Número de observações (j)')
# plt.ylabel('Viés Empírico')
# plt.title('Evolução do Viés Empírico com o Número de Observações')
# plt.axhline(0, color='red', linestyle='--', label='Viés = 0')
# plt.legend()
# plt.grid(True)
# plt.show()
# fig.savefig('figures/viés_empírico.png', dpi=300)

# Conforme o número de observações aumenta, o viés empírico se aproxima de zero, indicando que o estimador é não viesado.

#! b)

# mse_empirico = []

# # Calcula o estimador para cada sub-amostra e para cada j
# for j in range(n):
#     theta_hats = np.mean(samples[:, :j], axis=1) / 2  # média amostral / 2 para cada sub-amostra até j
#     # print(theta_hats)
#     mse = np.mean((theta_hats - theta)**2)  # média dos desvios (estimadores - valor real)
#     mse_empirico.append(mse)

# # Gerar o gráfico do viés empírico
# fig = plt.figure(figsize=(10, 6))
# plt.plot(range(1, n + 1), mse_empirico, label='MSE Empírico de $\\hat{\\theta}_{i,j}$')
# plt.xlabel('Número de observações (j)')
# plt.ylabel('MSE Empírico')
# plt.title('Evolução do MSE Empírico com o Número de Observações')
# plt.axhline(0, color='red', linestyle='--', label='MSE = 0')
# plt.legend()
# plt.grid(True)
# plt.show()
# fig.savefig('figures/MSE_empírico.png', dpi=300)

# Conforme o número de observações aumenta, o MSE empírico se aproxima de zero. Isso confirma a expressão pro MSE encontrado quando tendemos n ao infinito.

#! c)

means = []
# Calcula o estimador para cada sub-amostra e para cada j
for j in range(n):
    mean_sample = np.mean(samples[:, :j], axis=1) # média amostral / 2 para cada sub-amostra até j
    means.append(np.mean(mean_sample / 2))

# Gerar o gráfico do viés empírico
fig = plt.figure(figsize=(10, 6))
plt.plot(range(1, n + 1), means, label='Média Amostral $X_{n}$')
plt.xlabel('Número de observações (j)')
plt.ylabel('Média Amostral')
plt.title('Evolução da Média Amostral com o Número de Observações')
plt.axhline(5, color='red', linestyle='--', label='$\\theta = 5$')
plt.legend()
plt.grid(True)
plt.show()
fig.savefig('figures/consistencia.png', dpi=300)

#! d)

