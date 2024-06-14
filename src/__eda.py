import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd
import numpy as np 
import streamlit as st 
from __import import Import

imp = Import()
dataset = imp.import_data()

class EDA:
    def __init___(self):
        self.X = dataset.iloc[:,:-1]
        self.y = dataset.iloc[:,-1:]
    
    def __plot(self):
        


