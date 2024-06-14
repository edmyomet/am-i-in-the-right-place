import pandas as pd 

class Import:
    def __init__(self):
        self.df = pd.read_csv(r'datasets\gps_sensor_data.csv',sep=',')
        self.df.columns = names=['index','UTC','PositionStatus','Latitude','LatitudeDirection','Longitude',
                                'LongitudeDirection','Speed','TimeStamp','Date','Unknown','Zone','Label']
        
    def __return_dataset(self):
        return self.df
    
    def import_data(self):
        return self.__return_dataset()
    

def main():
    imp = Import()
    
if __name__ == '__main__':
    pass