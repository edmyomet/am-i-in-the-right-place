import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from __import import Import

import_obj = Import()
dataset = import_obj.import_data()

class Encoder:
    def __init__(self):
        self.encoder = LabelEncoder()
        self.features = dataset.columns[:-1]
        self.label = dataset.Label
        
    def __encode(self):
        self.label = self.encoder.fit_transform(self.label)
        dataset.Label = self.label
    
    def encode_label(self):
        self.__encode()
        dataset.to_csv(r'.\datasets\gps_sensor_data.csv')
        

if __name__ == '__main__':
    encoder = Encoder()
    encoder.encode_label()
