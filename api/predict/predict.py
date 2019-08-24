import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import os
def predict(school_level,doubts_asked,discussion,parent,absent):
    c_path = os.getcwd()
    c_path = os.path.join(c_path,'machine_learning','trained_model.sav')
    loaded_model = pickle.load(open(c_path,'rb'))
    pred = loaded_model.predict([[school_level,doubts_asked,discussion,parent,absent]])
    return pred[0]