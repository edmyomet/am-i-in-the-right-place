from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.cluster import DBSCAN, KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import silhouette_score
import numpy as np 
import pandas as pd 
from tqdm import tqdm
from __import import Import
import seaborn as sns 
import matplotlib.pyplot as plt 

imp = Import()
dataset = imp.import_data()

class DBSCANClustering:
    def __init__(self):
        dataset.drop(['index', 'Altitude','AltitudeUnit'], axis=1, inplace=True)
        self.X = dataset.iloc[:,:-1]
        self.X.drop(['LatitudeDir','LongitudeDir'],axis=1,inplace=True)
        
    def __model(self):
        self.model = DBSCAN(eps=2/6371,min_samples=5,metric='haversine')
        self.X = np.array(self.X)
        self.category = self.model.fit_predict(np.radians(self.X))
        print(self.category[(self.category == 1)])
        
    def public(self):
        self.__model()
        
class KMeansClustering:
    def __init__(self):
        #dataset.drop(['index', 'Altitude','AltitudeUnit'], axis=1, inplace=True)
        self.X = dataset.iloc[:,:-1]
        self.class_predictions = None
        #self.X.drop(['LatitudeDir','LongitudeDir'],axis=1,inplace=True)
        pass
    
    def __model(self):
        best_k,best_silhouette=0,-1
        for k in tqdm(range(2, 10)):
            model = KMeans(n_clusters=k, random_state=1).fit(self.X)
            self.class_predictions = model.predict(self.X)
    
            curr_silhouette = silhouette_score(self.X, self.class_predictions)
            if curr_silhouette > best_silhouette:
                best_k = k
                best_silhouette = curr_silhouette
        fig,axes = plt.subplots(1,1,figsize=(10,8),squeeze=False)
        sns.scatterplot(x=self.X.Latitude,y=self.X.Longitude, hue=self.class_predictions, palette=sns.color_palette('Spectral'),ax=axes[0][0])
        plt.savefig(r'static\images\classification.png')
    
    def __get_predictions(self):
        self.X['ClassLabel'] = self.class_predictions
        self.X.to_csv(r'datasets\classified_dataset.csv')
    def public(self):
        self.__model()
        self.__get_predictions()
        print(self.X)
        
def main():
    db = DBSCANClustering()
    db = KMeansClustering()
    db.public()
    
    
    
if __name__ == '__main__':
    main()