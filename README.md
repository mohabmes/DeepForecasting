# DeepForecasting
DeepForecasting is an intelligent decision support system used to predict the future company's stock price considering its stock historical data and news effect. To assist the nonfinancial expert users, we create a composite index for each company based on the best result returned from three different types of deep learning neural networks (Backpropagation, Radial Basis Function, and Recurrent) and the result obtained from the sentiment analysis of company's related news. This composite index is scored up to three, and higher values indicate more safety decisions.

[DeepForecasting-Plus](https://github.com/MichaelMarkos/DeepForecasting): Displayed the stock market prediction summaries in a friendly web user interface including visualized plots and informative reports. [[Screenshot](https://drive.google.com/file/d/19Sa2JQCDH_C6dx2r7PkgjhbfhSSgweJZ)]

## How to use
- Download Historical Data and generate the visualized plots. `python pystocklib/auto.py <ticker>`
> `python pystocklib/auto.py AMZN`
- Retrain model. `python stocknn/auto.py <ticker> --retrain`
> `python stocknn/auto.py AMZN --retrain`
```
python stocknn/auto.py [ticker] [operation]
[operation]:
    --retrain            Retrain an existing model.
    --train              Create a new model. [override any pre-existed model]
    --test               Load the model & print predicted value.
```
- PHP interface `php auto.php <ticker>`
```
php auto.php [ticker] [operation]
[operation]:
    --retrain            Retrain an existing model. (Default)
    --train              Create a new model. [override any pre-existed model]
    --test               Load the model & print predicted value.
```

### Requirement
- Python
- Keras
- PHP
- Scikit-learn
- Numpy
- Pandas
- Matplotlib
- Textblob
- Matplotlib
- bs4

### Credit
- [SaraEl-Metwally](https://github.com/SaraEl-Metwally)
- [AndrewRPorter](https://github.com/AndrewRPorter)
- [parkus](https://github.com/parkus)
- [PetraVidnerova](https://github.com/PetraVidnerova)
