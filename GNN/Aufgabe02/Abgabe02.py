import numpy as np


# Sigmoide Aktivierungsfunktion und ihre Ableitung
def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Sigmoidfunktion


def deriv_sigmoid(x):
    return x * (1 - x)  # Ableitung der Sigmoiden


# Das XOR-Problem, input [bias, x, y] und Target-Daten
inp = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
target = np.array([[0], [1], [1], [0]])

# Die Architektur des neuronalen Netzes
inp_size = 3  # Eingabeneuronen
hid_size = 4  # Hidden-Neuronen
out_size = 1  # Ausgabeneuron

# Gewichte zufällig initialisieren (Mittelwert = 0)
w0 = np.random.random((inp_size, hid_size)) - 0.5
w1 = np.random.random((hid_size, out_size)) - 0.5

delta_w0 = np.full_like(w0, 0.125)
delta_w1 = np.full_like(w1, 0.125)
delta_max = 50  # Maximale Gewichtsänderung
delta_min = 0  # Minimale Gewichtsänderung
eta_plus = 1.2  # Faktor zur Vergrößerung der Lernrate
eta_minus = 0.5  # Faktor zur Verkleinerung der Lernrate
grad_old_w0 = np.zeros_like(w0)
grad_new_w0 = np.zeros_like(w0)
grad_old_w1 = np.zeros_like(w1)
grad_new_w1 = np.zeros_like(w1)

# Netzwerk trainieren
for i in range(100000):

    # Vorwärtsaktivierung
    L0 = inp
    L1 = sigmoid(np.matmul(L0, w0))
    L1[0] = 1  # Bias-Neuron in der Hiddenschicht
    L2 = sigmoid(np.matmul(L1, w1))

    # Fehler berechnen
    # L2_error = target - L2

    # Backpropagation
    # L2_delta = L2_error * deriv_sigmoid(L2)
    # L1_error = np.matmul(L2_delta, w1.T)
    # L1_delta = L1_error * deriv_sigmoid(L1)

    # Gradienten berechnen
    grad_old_w0 = np.copy(grad_new_w0)
    grad_new_w0 = np.dot(L0.T, (L1 - target))
    grad_old_w1 = np.copy(grad_new_w1)
    grad_new_w1 = np.dot(L1.T, (L2 - target))

    # Gewichte aktualisieren
    for i in range(hid_size):
        for j in range(inp_size):
            if grad_old_w0[j, i] * grad_new_w0[j, i] > 0:  # Lernrate vergrößern
                delta_w0[j, i] = min(delta_w0[j, i] * eta_plus, delta_max)
            elif grad_old_w0[j, i] * grad_new_w0[j, i] < 0:  # Lernrate verkleinern
                delta_w0[j, i] = max(delta_w0[j, i] * eta_minus, delta_min)
                grad_new_w0[j, i] = 0  # Einziger Unterschied zu Rprop
    w0 -= delta_w0 * np.sign(grad_new_w0)

    for i in range(out_size):
        for j in range(hid_size):
            if grad_old_w1[j, i] * grad_new_w1[j, i] > 0:  # Lernrate vergrößern
                delta_w1[j, i] = min(delta_w1[j, i] * eta_plus, delta_max)
            elif grad_old_w1[j, i] * grad_new_w1[j, i] < 0:  # Lernrate verkleinern
                delta_w1[j, i] = max(delta_w1[j, i] * eta_minus, delta_min)
                grad_new_w1[j, i] = 0  # Einziger Unterschied zu Rprop
    w1 -= delta_w1 * np.sign(grad_new_w1)

# Netzwerk testen
L0 = inp
L1 = sigmoid(np.matmul(inp, w0))
L1[0] = 1  # Bias-Neuron in der Hiddenschicht
L2 = sigmoid(np.matmul(L1, w1))

print(L2)
