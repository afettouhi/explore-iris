import pandas as pd

sql_query = 'SELECT T.Name, A.Title FROM Track T ' \
            'JOIN Album A on T.AlbumId = A.AlbumId LIMIT 5'

df = pd.read_sql(sql_query, 'sqlite:///data/Chinook_Sqlite.sqlite')

df.boxplot()
