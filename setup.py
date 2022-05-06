from setuptools import setup
setup(
    name='StockGrabber',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'StockGrabber=StockGrabber:run'
        ]
    }
)