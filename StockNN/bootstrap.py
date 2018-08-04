import RNN as RNN
import RBF as RBF
import BKP as BKP



def determin_model(stock_name, scaler, X_train, X_test, y_train, epochs = 50, path=""):
    # path of the old model
    print("RNN Training ...")
    regressor = RNN.train(X_train, y_train, epochs = epochs)
    print("save Trained model ...")
    RNN.save_model(stock_name, regressor, path=path)
    model_path = path + "{}-RNN.h5".format(stock_name)
    _, rnn_mape = RNN.test(model_path, scaler, X_test)


    print("RBF Training ...")
    regressor = RBF.train(X_train, y_train, epochs = epochs)
    print("save Trained model ...")
    RBF.save_model(stock_name, regressor, path=path)
    model_path = path + "{}-RBF.h5".format(stock_name)
    _, rbf_mape = RBF.test(model_path, scaler, X_test)


    print("BKP Training ...")
    regressor = BKP.train(X_train, y_train, epochs = epochs)
    print("save Trained model ...")
    BKP.save_model(stock_name, regressor, path=path)
    model_path = path + "{}-BKP.h5".format(stock_name)
    _, bkp_mape = BKP.test(model_path, scaler, X_test)
    
    print("RNN: " + str(rnn_mape))
    print("RBF: " + str(rbf_mape))
    print("BKP: " + str(bkp_mape))
    
    if rnn_mape < rbf_mape and rnn_mape < bkp_mape:
        return "RNN"
    elif rbf_mape < rnn_mape and rbf_mape < bkp_mape:
        return "RBF"
    else:
        return "BKP"

