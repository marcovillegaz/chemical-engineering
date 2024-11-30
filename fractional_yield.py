import matplotlib.pyplot as plt
import numpy as np

phi = np.vectorize(lambda Ca: 6.09 * Ca / (6.09 * Ca + 1.81 * Ca**2))

Ca_array = np.linspace(0.1, 2, 20)
phi_array = phi(Ca_array)


plt.plot(Ca_array, phi_array)
plt.xlabel("Concentration de A")
plt.ylabel("Rendimiento fraccional")
plt.grid(True)
plt.show()
