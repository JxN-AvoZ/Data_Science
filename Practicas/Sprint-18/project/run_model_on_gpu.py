
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras.applications.resnet import preprocess_input, ResNet50
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam


def load_train(path):
    """
    Carga la parte de entrenamiento del conjunto de datos desde la ruta.
    Aplica aumentos de datos para mejorar la generalización.
    """
    labels = pd.read_csv(path + 'labels.csv')
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.25,
        horizontal_flip=True,
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1
    )
    train_gen_flow = train_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path,
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='training',
        seed=12345
    )
    return train_gen_flow


def load_test(path):
    """
    Carga la parte de validación/prueba del conjunto de datos desde la ruta.
    Solo aplica rescale, sin aumentos de datos.
    """
    labels = pd.read_csv(path + 'labels.csv')
    test_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.25
    )
    test_gen_flow = test_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path,
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='validation',
        seed=12345
    )
    return test_gen_flow


def extract_embeddings(path):
    labels = pd.read_csv(path + 'labels.csv')

    backbone = ResNet50(input_shape=(224, 224, 3),
                        weights='imagenet',
                        include_top=False,
                        pooling='avg')
    backbone.trainable = False

    datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
    flow = datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path,
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        shuffle=False
    )

    print("Extrayendo embeddings...")
    embeddings = backbone.predict(flow, verbose=1)
    ages = labels['real_age'].values

    return embeddings, ages


def create_model(input_shape):
    """
    Define el modelo de capas densas para regresión de edad.
    Recibe embeddings de 2048 dimensiones generados por ResNet50.
    """
    model = keras.Sequential([
        Input(shape=input_shape),
        Dense(256, activation='relu'),
        Dropout(0.4),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(1, activation='relu')
    ])

    model.compile(
        optimizer=Adam(learning_rate=0.0005),
        loss='mse',
        metrics=['mae']
    )
    return model


def train_model(model, X_train, y_train, X_test, y_test, epochs=100, batch_size=64):
    """
    Entrena el modelo de capas densas sobre los embeddings.
    Usa EarlyStopping para detener el entrenamiento en el mejor punto.
    """
    callbacks = [
        EarlyStopping(monitor='val_mae', patience=10, restore_best_weights=True),
        ModelCheckpoint('best_model.keras', monitor='val_mae', save_best_only=True)
    ]
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=callbacks,
        verbose=2
    )
    print(f"\nMejor val_mae: {min(history.history['val_mae']):.4f}")
    return model



if __name__ == '__main__':
    path = 'dataset/UTKFace/'

    # Estrategia de dos pasos:
    # 1. Extraer embeddings con ResNet50 (una sola vez)
    # 2. Entrenar capas densas sobre los embeddings

    embeddings, ages = extract_embeddings(path)
    np.save('embeddings.npy', embeddings)
    np.save('ages.npy', ages)
    print(f"Embeddings: {embeddings.shape}, Ages: {ages.shape}")

    X_train, X_test, y_train, y_test = train_test_split(
        embeddings, ages, test_size=0.25, random_state=12345
    )

    model = create_model((2048,))
    model = train_model(model, X_train, y_train, X_test, y_test)
