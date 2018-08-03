import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def preprocess(path):
    # Importing the dataset
    ds = pd.read_csv(path)
    dataset = ds.iloc[:, [2,5]].values
    
    X = ds.iloc[:, 2].values
    y = ds.iloc[:, 5].values
    
    # Feature Scaling
    scaler  = MinMaxScaler(feature_range=(0, 1))
    dataset_scaled = scaler.fit_transform(dataset)
    
    X = dataset_scaled[:, 0]
    y = dataset_scaled[:, 1]
    
    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    
#    # Sizes of train_ds, test_ds
#    dataset_sz = X.shape[0]
#    train_sz = X_train.shape[0]
#    test_sz = X_test.shape[0]
    
    return scaler, X_train, X_test, y_train, y_test