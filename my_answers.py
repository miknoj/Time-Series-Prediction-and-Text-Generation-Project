
import string

from keras.models import Sequential
from keras.layers import Activation
from keras.layers import Dense
from keras.layers import LSTM
import keras
import numpy as np


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    for i in range(len(series)-window_size):
        X.append(series[i:window_size+i])
    y = series[window_size:]

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(input_shape=(window_size, 1), units=5))
    model.add(Dense(1))

    return model

### TODO: return the text input with only ascii lowercase and the punctuation given 
### below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    ascii = string.ascii_letters
    
    for ch in set(text):
        if ch not in punctuation and ch not in ascii:
            text = text.replace(ch, ' ')

    return text

### TODO: fill out the function below that transforms the input text and window-size
### into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    for i in range(0, len(text) - window_size, step_size):
        inputs.append(text[i:i+window_size])
    outputs = text[window_size:len(text):step_size]
    
    return inputs, outputs

### TODO build the required RNN model: a single LSTM hidden layer with softmax
### activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(input_shape=(window_size, num_chars), units=200))
    model.add(Dense(num_chars))
    model.add(Activation('softmax'))
    return model
