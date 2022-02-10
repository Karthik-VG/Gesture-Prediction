import pandas as pd
import numpy as np
import os

class Data_loader:
    def __init__(self):
        pass
    
    def load_bulk_data(self,folder_path):
        data_folder = os.listdir(folder_path)
        data_folder.remove("README.txt")
        bulk_data=pd.DataFrame()

        temp=pd.DataFrame()
        for folder in data_folder:
            path=folder_path+"\\"+folder
            for files in os.listdir(path):
                file_path=path+"\\"+files
                print(file_path)
                df=pd.read_csv(file_path,sep="\s+")
                temp=pd.concat([temp,df],axis=0,ignore_index=True)

        return temp



data=Data_loader().load_bulk_data(r"D:\ineuron\ineuron internship\2.Gesture prediction using EEG data\Gesture Prediction\Gesture-Prediction\data\EMG_data_for_gestures-master")
print(data)