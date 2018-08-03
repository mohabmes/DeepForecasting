import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import load_model
from err import error_count, calc_diff, mape
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
#from visual import plot


def train(X_train, y_train, epochs = 50):
    regressor = Sequential()
    
    # Adding the input layer and the first hidden layer and Drop out Regularization
    regressor.add(Dense(units = 500, kernel_initializer = 'uniform', activation = 'relu', input_dim = 1))
    regressor.add(Dropout(.2))
    
    # Adding the first hidden layer and Drop out Regularization
    regressor.add(Dense(units = 500, kernel_initializer = 'uniform', activation = 'relu'))
    regressor.add(Dropout(.2))
    
    # Adding the second hidden layer and Drop out Regularization
    regressor.add(Dense(units = 500, kernel_initializer = 'uniform', activation = 'relu'))
    regressor.add(Dropout(.2))
    
    # Adding the third hidden layer and Drop out Regularization
    regressor.add(Dense(units = 500, kernel_initializer = 'uniform', activation = 'relu'))
    regressor.add(Dropout(.2))
    
    # Adding the output layer
    regressor.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    
    # Compiling the ANN
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    
    # Fitting the ANN to the Training set
    regressor.fit(X_train, y_train, batch_size = 32, epochs = epochs)
    
    return regressor


def save_model(name, regressor, path=str):
    # Save Trained Model
    regressor.save('{}{}-BKP.h5'.format(path, name))


def retrain(model_path, X_train, y_train, epochs):
    # load Trained Model
    regressor = load_model(model_path)
        # Compiling the ANN
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    
    # Fitting the ANN to the Training set
    regressor.fit(X_train, y_train, batch_size = 32, epochs = epochs)
    
    return regressor



def test(model_path, scaler, X_test):
    
    regressor = load_model(model_path)
    
    real_stock_price = np.array(X_test)
    inputs = real_stock_price
    predicted_stock_price = regressor.predict(inputs)
    
    # rebuild the Structure
    dataset_test_total = pd.DataFrame()
    dataset_test_total['real'] = real_stock_price
    dataset_test_total['predicted'] = predicted_stock_price
    
    # real data price VS. predicted price
    predicted_stock_price = scaler.inverse_transform(dataset_test_total) 
    
    # Calc difference between real data price and predicted price
    _mape = mape(predicted_stock_price[:, 0], predicted_stock_price[:, 1])
    
    # MSE
    _mse = mean_squared_error(predicted_stock_price[:, 0], predicted_stock_price[:, 1])
    
    return _mse, _mape


def predict(model_path, scaler, X):
        
    regressor = load_model(model_path)
    
    x = np.array([X])
    yh = regressor.predict(x)
    
    # rebuild the Structure
    x_yh = pd.DataFrame()
    x_yh['x'] = x
    x_yh['yh'] = yh
    
    # real test data price VS. predicted price
    x_yh = scaler.inverse_transform(x_yh)

    return x_yh[0]
