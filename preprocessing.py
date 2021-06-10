import numpy as np
import pandas as pd
import sklearn

test_path = 'data/test.csv'
train_path = 'data/train.csv'

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

from sklearn.feature_selection import chi2, f_regression, f_classif, mutual_info_classif,\
mutual_info_regression 
from sklearn.feature_selection import SelectKBest, SelectFromModel, VarianceThreshold
from sklearn import preprocessing
