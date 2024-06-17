from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.cluster import DBSCAN, KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score,recall_score,precision_score,accuracy_score,confusion_matrix
import numpy as np 
import pandas as pd 
from tqdm import tqdm
from __import import Import
import seaborn as sns 
import matplotlib.pyplot as plt 



dataset = pd.read_csv(r'datasets\classified_dataset.csv')

class KneighboursClassification:
    def __init__(self):
        self.X = dataset.iloc[:,1:-1]
        self.X.drop(['LatitudeDir','LongitudeDir'],axis=1,inplace=True)
        self.y = dataset.iloc[:,-1:]
        self.model = KNeighborsClassifier()
        self.scores = {'F1':None, 'precision':None, 'Accuracy':None, 'Recall':None}
    
    def __train_test_split(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y,test_size=0.25, random_state=21)
    
    def __build(self):
        
        self.model.fit(self.X_train, self.y_train)
    
    def __test(self,prediction_data=None,predict=False):
        if predict == False:
            self.y_pred = self.model.predict(self.X_test)
            self.scores['F1'] = f1_score(self.y_test, self.y_pred,average='micro')
            self.scores['precision'] = precision_score(self.y_test, self.y_pred,average='micro')
            self.scores['Accuracy'] = accuracy_score(self.y_test, self.y_pred)
            self.scores['Recall'] = recall_score(self.y_test, self.y_pred,average='micro')
            print(self.scores)
            fig,axes = plt.subplots(1,1,figsize=(10,8),squeeze=False)
            sns.heatmap(confusion_matrix(self.y_test,self.y_pred),ax=axes[0][0])
            plt.savefig(r'static\images\cmatrix.png')
        else:
            prediction_data = np.array(list(prediction_data.values())).reshape(1,-1)
            df = pd.DataFrame(prediction_data,columns=['Latitude','Longitude'])
            self.y_pred = self.model.predict(df)
            
        
    def test_model(self, **kwargs):
        self.__test(prediction_data=kwargs['prediction_data'], predict=kwargs['predict'])
    def public(self):
        self.__train_test_split()
        self.__build()
        self.__test()

def main():
    knn = KneighboursClassification()
    knn.public()
    
    
if __name__ == '__main__':
    main()