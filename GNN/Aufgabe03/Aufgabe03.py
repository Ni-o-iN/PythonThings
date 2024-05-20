import numpy as np
import matplotlib.pyplot as plt
from keras.api.datasets import fashion_mnist
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

# Laden Sie den Fashion MNIST-Datensatz
(x_train, _), (x_test, _) = fashion_mnist.load_data()

# Normalisieren Sie die Pixelwerte auf [0, 1]
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

# Ändern Sie die Form der Bilder in eine eindimensionale Darstellung
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

# Definieren Sie die RBM mit 100 Hidden Neuronen
rbm = BernoulliRBM(n_components=100, learning_rate=0.01, batch_size=10, n_iter=10, random_state=0)

# Daten skalieren
scaler = MinMaxScaler()

# Pipeline für Skalierung und RBM
rbm_pipeline = Pipeline(steps=[('scaler', scaler), ('rbm', rbm)])

# RBM trainieren
rbm_pipeline.fit(x_train)

# Daten transformieren
X_scaled = scaler.transform(x_test)
X_transformed = rbm.transform(X_scaled)

# Manuelle Rekonstruktion der Daten
X_reconstructed = X_transformed @ rbm.components_ + rbm.intercept_visible_
X_reconstructed = scaler.inverse_transform(X_reconstructed)


# Funktion zur Visualisierung der Original- und Rekonstruktionsbilder
def plot_digits(orig, recon, n=10):
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # Original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(orig[i].reshape(28, 28), cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Rekonstruiert
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(recon[i].reshape(28, 28), cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()


# Original- und rekonstruierte Bilder anzeigen
plot_digits(x_test, X_reconstructed)
