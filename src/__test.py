import numpy as np 
from __predict import KneighboursClassification
import pynmea2
import pandas as pd 
import serial

gps_writer = serial.Serial('COM3',9600)
knn = KneighboursClassification()
knn.public()
value_list = {'Latitude':None, 'Longitude':None}

def read_nmea_dump():
    count = 0
    with open(r'datasets\parsed_data.txt','r') as gps_dump:
        while gps_dump.read(1):
            data = gps_dump.readline()
            data = pynmea2.parse(data)
            if isinstance(data, pynmea2.types.talker.GGA):
                value_list['Latitude'] = data.latitude
                value_list['Longitude'] = data.longitude
                knn.test_model(prediction_data=value_list,predict=True)
    
def classify_input():
    for data in knn.y_pred:
        if data == 0 or data == 6 or data == 7:
            print('point is within the fence')
            gps_writer.write('You are within the fence'.encode())
        else:
            print('You are outside the fence')
            gps_writer.write('You are outside the fence'.encode())
            


def main():
    read_nmea_dump()
    classify_input()
    
    
if __name__ == '__main__':
    main()