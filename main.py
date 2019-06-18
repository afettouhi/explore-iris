import seaborn as sns
import matplotlib.pyplot as plt

all_datasets = sns.get_dataset_names()
dataset = sns.load_dataset('iris')

#%%
dataset.shape
dataset.head()
dataset.tail()
dataset.describe()
dataset.sample(3)
dataset.isnull().sum()

#%%
dataset.plot(kind='box')
plt.show()

#%%
sns.set_style('ticks')
sns.boxplot(data=dataset)
plt.show()

#%%
dataset.hist()
plt.show()

#%%
sns.swarmplot(x='species', y='petal_length', data=dataset)
plt.show()

#%%
from pandas.plotting import scatter_matrix
scatter_matrix(dataset)
plt.show()

#%%
import sqlite3

db = sqlite3.connect('data/Chinook_Sqlite.sqlite')
cursor = db.cursor()
sql_query = 'SELECT * FROM Track T ' \
            'JOIN Album A on T.AlbumId = A.AlbumId LIMIT 5'

cursor.execute(sql_query)
all_rows = cursor.fetchall()
for r in all_rows:
    print(str(r))

db.close()
