import tensorflow as tf
from tensorflow.keras.layers import Lambda
from tensorflow.keras.regularizers import l1,l2,l1_l2
from kerastuner import HyperModel
import kerastuner as kt
import json
import os 
from config import  *
import pandas as pd
import numpy as np

class MyHyperModel(HyperModel):
    def __init__(self, num_classes):
        self.num_classes = num_classes
        
    def build(self, hp):
        inputs = tf.keras.Input(shape=INPUT_SHAPE)
        MIN_VALUE = FINE_TUNE_LAYERS['MIN_VAL']
        MAX_VALUE = FINE_TUNE_LAYERS['MAX_VAL']
        flatten = tf.keras.layers.Flatten()
        x = flatten(inputs)
        MIN_VAL = FC_LAYERS['MIN_VAL']
        MAX_VAL = FC_LAYERS['MAX_VAL']
        for i in range(hp.Int('num_layers', MIN_VAL, MAX_VAL)):
            layer = tf.keras.layers.Dense(units=hp.Int('units_' + str(i),
                                            min_value=128,
                                            max_value=4096,
                                            step=32))
            x = layer(x)
            x = tf.keras.layers.GaussianNoise(stddev = hp.Float('gaussian_noise_'+str(i),
                                                                min_value = 0.1,
                                                                max_value = 0.9,
                                                                sampling = 'log'))(x)
            if MODEL_CONF['BATCH_NORM'] == True:
                batch_norm = tf.keras.layers.BatchNormalization()
                x = batch_norm(x)
            x = tf.keras.activations.relu(x)
            if MODEL_CONF['REGULARIZATION'] == True:
                gaussian_dropout = tf.keras.layers.GaussianDropout(rate=hp.Float('gaussian_dropout_'+str(i),
                                                                                 min_value = 0.1,
                                                                                 max_value = 0.9,
                                                                                 sampling = 'log'))
                x = gaussian_dropout(x)
            dropout = tf.keras.layers.Dropout(0.2)
            x = dropout(x)
            
        if len(N_LABELS) == 2:
            prediction_layer = tf.keras.layers.Dense(1,activation='sigmoid')
            outputs = prediction_layer(x)
            model = tf.keras.Model(inputs,outputs)
            model.compile(loss = tf.keras.losses.BinaryCrossentropy(from_logits=False),
                    optimizer = "adam",
                    metrics = ['accuracy'])
            
            return model
        elif len(N_LABELS) > 2:
            prediction_layer = tf.keras.layers.Dense(N_LABELS,activation='softmax')
            outputs = prediction_layer(x)
            model = tf.keras.Model(inputs,outputs)
            model.compile(loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                    optimizer = "adam",
                    metrics = ['accuracy'])
            
            return model
    

def prepare_dataset():
    data = pd.read_csv(DATAPATH)
    x_columns = list(set(data.columns)-set(LABEL_NAME))
    y_columns = [LABEL_NAME]

    x_data = data[x_columns].to_numpy()
    y_data = data[y_columns].to_numpy()

    return x_data,y_data