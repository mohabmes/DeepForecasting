from pystocklib import *

# Get the historical data
hist = HistoricalData('BTC-USD', from_date=[2018, 1, 1], to_date=[2018, 4, 4])
hist.create_csv()

# # Apply EMD & show the figures
price = hist.get_close()
emd = EMD(price)
emd.save_figure('AAPL')
emd.save_figure('AAPL-trend', type='trend') # type => trend, all, modes, ds
#
#
# sd = hist.standard_deviation('Open')
# print(sd)
#
# # get recent News
# news = News('Apple')
# result = news.get_result()
# print(result)
