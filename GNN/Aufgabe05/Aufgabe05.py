import numpy as np
import matplotlib.pyplot as plt

# Tangens-Hyperbolicus-Transferfunktion
def tanh(x):
    return 2 / (1 + np.exp(-2 * x)) - 1

# Gewichte
wbias1 = -3.37
wbias2 = 0.125
w11 = -4
w12 = 1.5
w21 = -1.5
w22 = 0

# Anfangswerte
o1, o2 = 0.0, 0.0

# Listen zur Speicherung der Outputs
o1_list = []
o2_list = []

# Iterationen
for _ in range(50):
    net1 = w11 * o1 + w12 * o2 + wbias1
    net2 = w21 * o1 + w22 * o2 + wbias2
    o1 = tanh(net1)
    o2 = tanh(net2)
    o1_list.append(o1)
    o2_list.append(o2)

# Visualisierung
plt.plot(o1_list, label='o1')
plt.plot(o2_list, label='o2')
plt.xlabel('Iterationen')
plt.ylabel('Output')
plt.legend()
plt.title('Ausgabe von o1 and o2 über Iterationen')
plt.grid(True)
plt.show()
