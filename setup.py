from distutils.core import setup

setup(
	name='DeepForecasting',
	version='1.0',
	packages=['pystocklib.pystocklib', 'pystocklib.pystocklib.emd_lib', 'pystocklib.pystocklib.yahoo_historical'],
	install_requires=['keras', 'scikit-learn', 'pandas', 'scipy', 'textblob', 'numpy', 'matplotlib', 'bs4', 'tld'],
	url='https://github.com/mohabmes/DeepForecasting',
	license='MIT',
	author='mohabmes',
	author_email='mohab.elsheikh@gmail.com',
	description='An open source AI financial Python tool with PHP interface used to provide a brief report that include the predicted future price of a stock using neural networks, measure the risk rate, evaluate the current state by analyzing the recent news, extract the trend signal, and provide visualization.'
)
