import pandas as pd
'''
test.csv中记录了一批文件的目录，目录名前面都多加了/home/inspurfs/user-fs，要求把它删除掉
BB代表列名
'''
data = pd.read_csv('test.csv')
data['BBB'] = data['BBB'].astype(str)
data['BBB'] = data['BBB'].apply(lambda x: x.replace('/home/inspurfs/user-fs', ''))
data.to_csv('test.csv', index=False)
