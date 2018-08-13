import os
import sys
import json
import preprocess as prep
import helper as hlp

config = hlp.load_config()

model_type_file = ""
model_type = ""
stock_name = ""
path = config["data_dir"] + "{}\\"
epochs_num_to_determin_model = config['nn_setups']['epochs_num_to_determin_model']
epochs_num = config['nn_setups']['epochs_num']
op = ""


if sys.argv[0] and sys.argv[1] and sys.argv[2] != "":
    op = sys.argv[2]
    stock_name = sys.argv[1]
    path = path.format(stock_name)
    model_type_file = path + "model.txt"
    print(path)

if not os.path.exists(path):
    error = "error : '{}' Not Found!".format(path)
    print(error)
    exit()

print("Reading csv file ...")
csv_path = path + "{}.csv".format(stock_name)

print("Dataset preprocessing ...")
scaler, X_train, X_test, y_train, y_test = prep.preprocess(csv_path)

    
if not os.path.isfile(model_type_file):
    from bootstrap import determin_model

    print("Training phase ...")
    model_type = determin_model(stock_name, scaler, X_train, X_test, y_train, path=path, epochs=epochs_num_to_determin_model)

    hlp.write_file(model_type_file, model_type)
    
else:
    model_type = hlp.read_file(model_type_file)
    print(model_type)

    if model_type == "RNN":
        import RNN as dl
    elif model_type == "RBF":
        import RBF as dl
    elif model_type == "BKP":
        import BKP as dl

    if op == "--train":
        regressor = dl.train(X_train, y_train, epochs = epochs_num)
        dl.save_model(stock_name, regressor, path=path)

    elif op == "--retrain":
        # path of the old model
        old_model = path + "{}-{}.h5".format(stock_name, model_type)
        regressor = dl.retrain(old_model, X_train, y_train, epochs = epochs_num)
        dl.save_model(stock_name, regressor, path=path)

    elif op == "--test":
        # path of the old model
        model_path = path + "{}-{}.h5".format(stock_name, model_type)
        _mse, _mape = dl.test(model_path, scaler, X_test)
        print(_mse, _mape)


X = X_test[len(X_test) - 1]

print("prediction ...")
model_path = path + "{}-{}.h5".format(stock_name, model_type)
prediction = dl.predict(model_path, scaler, X)
print(str(prediction[1]))

hlp.write_file(path + "prediction.txt", str(prediction[1]))