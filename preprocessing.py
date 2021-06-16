import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print(check_output(["ls", "data"]).decode("utf8"))

# Any results you write to the current directory are saved as output.

# for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# import data
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

for i in range(train.shape[1]):
	if(train.iloc[:,i].isnull().sum()>0):
		print(list(train.columns.values)[i] + ": " + str(train.iloc[:,i].isnull().sum()))

ax = sns.distplot(train['SalePrice'])
plt.show()

train['SalePrice'] = np.log(train['SalePrice'])

ax = sns.distplot(train['SalePrice'])
plt.show()

print(train.shape[0])