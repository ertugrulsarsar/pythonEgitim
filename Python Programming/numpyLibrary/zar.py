# NumPy ile rastgele zar atışları yapılarak sonuçların histogram grafiği çizilir.


import numpy as np
import matplotlib.pyplot as plt

# Rastgele zar atışları
zar_atilmalari = np.random.randint(1, 7, size=1000)

# Histogram çizimi
plt.hist(zar_atilmalari, bins=np.arange(1, 8) - 0.5, edgecolor="black")
plt.xticks(range(1, 7))
plt.xlabel("Zar Sonucu")
plt.ylabel("Frekans")
plt.title("Zar Atışları Histogramı")
plt.show()
