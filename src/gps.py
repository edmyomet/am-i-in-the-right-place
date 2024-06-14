import serial
import time
import pandas as pd
import numpy as np
import csv
import pynmea2

class GPSSerial:
    def __init__(self, port:str, baud_rate:int):
        self.port:str = port
        self.baud_rate:int = baud_rate
        self.gps_read:serial.serialwin32.Serial = serial.Serial(self.port, self.baud_rate, timeout=0)
        self.data:str = ""
        
    def __read_data(self)->str:
        data = self.gps_read.readline()
        data = data.decode(encoding='utf-8',errors='ignore').rstrip()
        return data

    def __load_gps_csv(self, filepath:str,category:int=0)->None:
        with open(filepath,'r') as file:
            while file.read(1):
                try:
                    data = file.readline()
                    data = pynmea2.parse(data)
                    if isinstance(data, pynmea2.types.talker.RMC):
                        data.data.append(category)
                        with open (r'.\datasets\gps_sensor_data.csv','a',newline='') as csv_file:
                            wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                            wr.writerow(data.data)
                except:
                    continue
            file.close()
    
    def get_gps_data(self)->None:
        try:
            while True:
                self.data = self.__read_data()
                if(self.data.startswith('$')):
                    print(self.data)
                    print(self.data)
                    with open(r'gps_data.txt','a') as txt_file:
                        txt_file.write(self.data+"\n")
                    time.sleep(2)
        except(KeyboardInterrupt):
            print(r'Key Press has stopped the process')
            txt_file.close()
    
    def gps_parser(self)->None:
        self.__load_gps_csv(r'.\datasets\points_inside.nmea',1)
        self.__load_gps_csv(r'.\datasets\points_outside.nmea')
        
            
        
    
        
    
def main():
    gps = GPSSerial('COM3', 9600)
    #gps.get_gps_data()
    gps.gps_parser()


if __name__ == '__main__':
    main()

    