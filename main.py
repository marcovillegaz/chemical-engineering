import numpy as np
import matplotlib.pyplot as plt

import reaction_kinetics.reactors as rk

# Example usage
Xa_o = np.linspace(0, 1, 20)
Xa_i = 0
Ca_i = 10
n = np.linspace(0.5, 1.5, 5)
k = 0.01

plt.figure(figsize=(8, 6))

for order in n:

    tau = rk.stirred_tank(Xa_o, Xa_i, Ca_i, order, k)

    plt.plot(Xa_o, tau, label=f"n = {order}")

plt.xlabel("Ca (Molar Concentration of A)")
plt.ylabel("tau (Residence Time)")
plt.title("Residence Time vs. Molar Concentration of A")
plt.legend()
plt.grid(True)
plt.show()


## stirred_tank.volume
## stirred_tank.flow
## stirred:tank.conversion

## rx = reactor(type,kinetic)
## rx.volume =
