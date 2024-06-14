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
        self.label = dataset.Category
        
    def __encode_label(self):
        self.label = self.encoder.fit_transform(self.label)
        dataset.Category = self.label
        
    def __encode_column(self,colname='LatitudeDir'):
        dataset.loc[dataset[colname] == 'N',colname] = 1
        dataset.loc[dataset[colname] == 'S', colname] = 2
        dataset.loc[dataset[colname] == 'E', colname] = 3
        dataset.loc[dataset[colname] == 'W', colname] = 4
        print(dataset)
        dataset.drop(['index'],inplace=True)
            
    
    def encode_label(self):
        self.__encode_label()
        self.__encode_column()
        self.__encode_column('LongitudeDir')
        dataset.to_csv(r'.\datasets\gps_sensor_data_new.csv')
        

if __name__ == '__main__':
    encoder = Encoder()
    encoder.encode_label()