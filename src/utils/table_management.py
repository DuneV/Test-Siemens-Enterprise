import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pylab as pyplot
from scipy import signal
from scipy.fft import fft, ifft, fftfreq
from scipy.signal import find_peaks
from scipy.signal import hilbert
from scipy.signal import stft
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d


class table_gen:
    def __init__(self, data, threshold, suavizar=True):
        """
        Creates a table as a dataframe with an SQL instance. 

        Parameters:
        data (str): Path to the CSV file containing the signal data.
        threshold (float): Threshold value for any analysis requiring it.
        """
        # Load the CSV file as a DataFrame
        self.data = data.copy()
        self.threshold = threshold
        self.signal = None
        self.frecuency = self.data.iloc[:, 0].replace(',', '.', regex=True)
        self.magnitude = self.data.iloc[:, 1].replace(',', '.', regex=True)


        self.frecuency = self.frecuency.astype(float)
        self.magnitude = self.magnitude.astype(float)

    
        self.linear_mg = self.magnitude.apply(lambda x: 10**(x/20))
        if suavizar:
            self.linear_mg = self.suavizar(window_length=11, polyorder=2)
        self.fs = 960 * 10 ** 6 # dos veces la frecuencia de muestreo
        self.resistance = 50