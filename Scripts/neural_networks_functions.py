# Data manipulation
import numpy as np
import pandas as pd

# Plotting
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import seaborn as sns

# Machine learning and preprocessing
from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Deep learning - TensorFlow/Keras
import shap
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import BatchNormalization, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

# Hyperparameter tuning
import keras_tuner as kt

def build_model(hp, input_dim):
    """
    Builds a neural network model using Keras Tuner for hyperparameter optimization.

    Args:
        hp (keras_tuner.HyperParameters): Hyperparameter search space.
        X_train (np.ndarray or pd.DataFrame): Normalized training feature set used to determine input dimensions.

    Returns:
        tensorflow.keras.models.Sequential: Compiled neural network model.
    """
    model = Sequential()

    # First dense layer
    model.add(
        Dense(
            units=hp.Int("units_layer1", min_value=64, max_value=256, step=16),
            activation="relu",
            input_dim= input_dim,
        )
    )
    model.add(BatchNormalization())
    model.add(
        Dropout(hp.Float("dropout_layer1", min_value=0.2, max_value=0.5, step=0.1))
    )

    model.add(
        Dense(
            units=hp.Int("units_layer1", min_value=32, max_value=128, step=16),
            activation="relu",
        )
    )
    model.add(BatchNormalization())
    model.add(
        Dropout(hp.Float("dropout_layer1", min_value=0.2, max_value=0.5, step=0.1))
    )

    # Second dense layer
    model.add(
        Dense(
            units=hp.Int("units_layer2", min_value=16, max_value=64, step=16),
            activation="relu",
        )
    )
    model.add(BatchNormalization())
    model.add(
        Dropout(hp.Float("dropout_layer2", min_value=0.2, max_value=0.5, step=0.1))
    )

    # Third dense layer
    model.add(
        Dense(
            units=hp.Int("units_layer3", min_value=8, max_value=32, step=16),
            activation="relu",
        )
    )
    model.add(BatchNormalization())
    model.add(
        Dropout(hp.Float("dropout_layer3", min_value=0.2, max_value=0.5, step=0.1))
    )

    # Output layer
    model.add(Dense(1, activation="sigmoid"))

    # Compile model
    model.compile(
        optimizer=Adam(
            learning_rate=hp.Float(
                "learning_rate", min_value=1e-4, max_value=1e-2, sampling="log"
            )
        ),
        loss="binary_crossentropy",
        metrics=["Recall", "Precision", "accuracy"],
    )

    return model


def plot_training_curves(history):
    """
    Plots training and validation loss, recall, and precision curves.

    Args:
        history (tensorflow.keras.callbacks.History): Training history object from model fitting.

    Returns:
        None
    """
    epochs = np.arange(len(history.history["loss"]))

    # Identify the best epoch (minimum validation loss)
    best_epoch = np.argmin(history.history["val_loss"])

    plt.figure(figsize=(12, 18))

    # Loss plot
    plt.subplot(3, 1, 1)
    plt.plot(epochs, history.history["loss"], label="Training")
    plt.plot(epochs, history.history["val_loss"], label="Validation")
    plt.axvline(best_epoch, linestyle="--", color="r", label=f"Best Epoch: {best_epoch}")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.title("Loss Curve")
    plt.legend()
    plt.grid(True)

    # Recall plot
    plt.subplot(3, 1, 2)
    plt.plot(history.history["recall"], label="Train Recall")
    plt.plot(history.history["val_recall"], label="Validation Recall")
    plt.axvline(best_epoch, linestyle="--", color="r", label=f"Best Epoch: {best_epoch}")
    plt.xlabel("Epochs")
    plt.ylabel("Recall")
    plt.title("Recall Curve")
    plt.legend()
    plt.grid(True)

    # Precision plot
    plt.subplot(3, 1, 3)
    plt.plot(epochs, history.history["precision"], label="Training")
    plt.plot(epochs, history.history["val_precision"], label="Validation")
    plt.axvline(best_epoch, linestyle="--", color="r", label=f"Best Epoch: {best_epoch}")
    plt.xlabel("Epochs")
    plt.ylabel("Precision")
    plt.title("Precision Curve")
    plt.legend()
    plt.grid(True)

    # Adjust spacing between plots
    plt.subplots_adjust(hspace=0.4)
    plt.show()