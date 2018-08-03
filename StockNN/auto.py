import os
import sys

model_type_file = ""
model_type = ""
stock_name = ""
path = "C:\\xampp\\htdocs\\deepforcasting\\tmpdata\\{}\\"
op = ""


if sys.argv[0] and sys.argv[1] and sys.argv[2] != "":
    op = sys.argv[2]
    stock_name = sys.argv[1]
    path = path.format(stock_name)
    model_type_file = path + "model.txt"
    print(path)
    
if not os.path.isfile(model_type_file):
    error = "error : '{}' Not Found!".format(model_type_file)
    print(error)
    
    from bootstrap import determin_model
    import preprocess as prep
    
    csv_path = path + "{}.csv".format(stock_name)
    scaler, X_train, X_test, y_train, y_test = prep.preprocess(csv_path)
    
    model_type = determin_model(stock_name, scaler, X_train, X_test, y_train, path=path, epochs=1)
    
    f=open(model_type_file, "w")
    f.write(model_type)
    f.close()
    
else:
    f=open(model_type_file, "r")
    model_type = f.read()
    print(model_type)


import preprocess as prep

if model_type == "RNN":
    import RNN as dl
elif model_type == "RBF":
    import RBF as dl
elif model_type == "BKP":
    import BKP as dl


if not os.path.exists(path):
    error = "error : '{}' Not Found!".format(path)
    print(error)
    exit()


csv_path = path + "{}.csv".format(stock_name)
scaler, X_train, X_test, y_train, y_test = prep.preprocess(csv_path)

X = X_test[len(X_test)-1]

if op == "--train":
    regressor = dl.train(X_train, y_train, epochs = 1)
    dl.save_model(stock_name, regressor, path=path)
    
    
elif op == "--retrain":
    # path of the old model
    old_model = path + "{}-{}.h5".format(stock_name, model_type)
    regressor = dl.retrain(old_model, X_train, y_train, epochs = 1)
    dl.save_model(stock_name, regressor, path=path)
    
elif op == "--test":
    # path of the old model
    model_path = path + "{}-{}.h5".format(stock_name, model_type)
    _mse, _mape = dl.test(model_path, scaler, X_test)
    print(_mse, _mape)


model_path = path + "{}-{}.h5".format(stock_name, model_type)
prediction = dl.predict(model_path, scaler, X)
print(str(prediction[1]))

f=open(path + "prediction.txt", "w")
f.write(str(prediction[1]))
f.close()


