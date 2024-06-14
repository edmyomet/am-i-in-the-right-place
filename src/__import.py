import pandas as pd 

class Import:
    def __init__(self):
        self.df = pd.read_csv(r'datasets\gps_sensor_data_new.csv',sep=',')
        self.df = self.df.iloc[:,1:]
        self.df.columns =['index','Latitude','LatitudeDir','Longitude','LongitudeDir','Altitude','AltitudeUnit','Category']
        
    def __return_dataset(self):
        for data in self.df['Latitude']:
            data = int(data)
        return self.df
    
    def import_data(self):
        return self.__return_dataset()
    

def main():
    imp = Import()
    imp.import_data()
    
if __name__ == '__main__':
    main()