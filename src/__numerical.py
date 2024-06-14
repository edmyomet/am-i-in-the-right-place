import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from __import import Import
from scipy.stats import pearsonr

imp_obj = Import()
dataset = imp_obj.import_data()


class DescriptiveStatistics:
    def __init__(self,category=1):
        self.label = category
        self.df = dataset[(dataset.Category==category)]
        self.feature_list = self.df.columns[:-1]
        
    def __info(self,feature:str='descr'):
        if feature != 'descr':
            print(self.df.info())
            self.df.head().to_csv(r'.\output\head.csv')
            self.df.tail().to_csv(r'.\output\tail.csv')
        else:
            self.df.describe().to_csv(r'.\output\scription.csv')
    def info(self):
        self.__info(feature='info')
        self.__info()
    

class Univariate(DescriptiveStatistics):
    def __init__(self,category):
        super().__init__(category=category)
        
    def __mean(self):
        self.mean = self.df.mean(numeric_only=True)
        self.mean.to_csv(rf'output\mean{self.label}.csv')
    
    def __median(self):
        self.median = self.df.median(numeric_only=True)
        self.median.to_csv(rf'output\median{self.label}.csv')
        
    def __mode(self):
        self.mode = self.df.mode(numeric_only=True)
        self.mode.to_csv(rf'output\mode{self.label}.csv')        

    def __range(self):
        self.range:dict[dict[str]] = {output_feature : {'min': None, 'max':None}for output_feature in self.feature_list}
        for feature in self.feature_list:
            try:
                self.range[feature]['min'] = self.df[feature].min(numeric_only=True)
                self.range[feature]['max'] = self.df[feature].max(numeric_only=True)
            except:
                print('Some non numeric features have been excluded')
                continue
        pd.DataFrame.from_dict(self.range, orient='index').to_csv(rf'output\range{self.label}.csv')
    
    def __std(self):
        self.std = self.df.std(numeric_only=True)
        self.std.to_csv(rf'output\std{self.label}.csv')
    
    def __skew(self):
        self.skew = self.df.skew(numeric_only=True)
        self.skew.to_csv(rf'output\skew{self.label}.csv')
    
    def __kurt(self):
        self.kurt = self.df.kurtosis(numeric_only=True)
        self.kurt.to_csv(rf'output\kurtosis{self.label}.csv')
        
    def public(self):
        self.info()
        self.__mean()
        self.__median()
        self.__mode()
        self.__std()
        self.__skew()
        self.__kurt()
        self.__range()
        

class Bivariate(DescriptiveStatistics):
    def __init__(self,category=1):
        super().__init__(category=category)
    
    def __cov(self):
        self.cov = self.df.cov(numeric_only=True)
        #print(self.df.corrwith(self.df['Label']))
        self.cov.to_csv(rf'output\cov{self.label}.csv')
    
    def __corr(self):
        self.corr = self.df.corr(numeric_only=True)
        self.corr.to_csv(rf'output\corr{self.label}.csv')
    
    

        
    def public(self):
        self.__cov()
        self.__corr()
    
    
def main():
    DS = Univariate(1)
    DS.public()
    DS = Bivariate(1)
    DS.public()
    
    
    
if __name__ == '__main__':
    main() 