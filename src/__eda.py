import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd
import numpy as np 
import streamlit as st 
from __import import Import
import folium
import io 
from PIL import Image
import selenium
sns.set_palette(palette=sns.color_palette('Spectral'))
imp = Import()
dataset = imp.import_data()
dataset = dataset.groupby('Category',group_keys=False).apply(lambda x:x.sample(100))

class EDA:
    def __init___(self):
        self.X = dataset.iloc[:,:-1]
        self.y = dataset.iloc[:,-1:]
    
    def __plot(self):
        fig,axes = plt.subplots(1,1,figsize=(10,8),squeeze=False)
        fig.suptitle('Plotting GPS')
        sns.scatterplot(x=dataset.Latitude, y=dataset.Longitude, hue=dataset.Category, palette=sns.color_palette('Spectral'),ax=axes[0][0])
        plt.savefig(r'static\images\plot.png')
    
    def __norm_distr(self):
        fig,axes = plt.subplots(1,4,figsize=(25,4),squeeze=False)
        x = dataset[(dataset.Category == 1)]['Latitude']
        sns.histplot(data=dataset,x=x,kde=True,ax=axes[0][0]).lines[0].set_color('black')
        x = dataset[(dataset.Category == 1)]['Longitude']
        sns.histplot(data=dataset,x=x,kde=True,ax=axes[0][1]).lines[0].set_color('black')
        x = dataset[(dataset.Category == 0)]['Latitude']
        sns.histplot(data=dataset,x=x,kde=True,ax=axes[0][2]).lines[0].set_color('black')
        x = dataset[(dataset.Category == 0)]['Longitude']
        sns.histplot(data=dataset,x=x,kde=True,ax=axes[0][3]).lines[0].set_color('black')
        plt.savefig(r'static\images\norm.png')
    
    def __folium_plot(self):
        map_obj = folium.Map(location=[dataset.Latitude.mean(),dataset.Longitude.mean()],zoom_start=10,tiles='OpenStreetMap',attr='<a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>')
        
        for _, row in dataset.iterrows():
            folium.CircleMarker(
                location = [row.Latitude, row.Longitude],
                radius = 3,
                color='#1787FE',
                fill=True,
                fill_color='#1787FE'
            ).add_to(map_obj)
            image_data = map_obj._to_png(5)
            image = Image.open(io.BytesIO(image_data))
            image.save(r'static\images\folium.png')
    
    def public(self):
        self.__plot()
        #self.__folium_plot()
        self.__norm_distr()
        
def main():
    eda = EDA()
    eda.public()

if __name__ == '__main__':
    main()
        

