import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f

# Parâmetros
alpha = 0.05
powers = [0.9]  # Poderes desejados
sample_sizes = range(1, 200, 1)
r_values = np.linspace(1.1, 2.0, 10)

# Inicializar o gráfico
plt.figure(figsize=(10, 6))

for power in powers:
    sizes_needed = []
    for r in r_values:
        r = 1.5
        for n in sample_sizes:
            df1 = df2 = n - 1
            f_critical = f.ppf(1 - alpha, df1, df2)
            non_central_param = (r - 1)**2 * n
            if f.cdf(f_critical, df1, df2, non_central_param) < power:
                sizes_needed.append(n)
                break
    
    plt.plot(r_values, sizes_needed, label=f'Power = {power}')

plt.xlabel('Razão das Variâncias (r)')
plt.ylabel('Tamanho Mínimo da Amostra Necessário')
plt.title('Tamanho da Amostra Necessário por Razão das Variâncias')
plt.legend()
plt.grid(True)
plt.show()
