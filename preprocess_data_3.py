import pandas as pd
import re
import os

# revised for original one miss some of the comments

def preprocess_data():
    df = pd.read_csv('vul_data_2.csv', header=None, skiprows=1)
    print(df.head(5))
    df.columns = ['number', 'cve_id', 'patch', 'summary']

    for index, item in enumerate(df['patch']):
        with open('/content/temp.c','w') as f:
          f.write(item)
        os.system("sh /content/remover.sh")
        with open('/content/tempRemoved.c','r') as f2:
          item = f2.read()
        print(item)
        item = re.sub(r'@@.*@@', " ", item)
        df.loc[index, 'patch'] = item
    # 同时处理 各种不同样式的注释
    df = df[['cve_id', 'patch', 'summary']]
    df.to_csv("vul_data_3.csv")


if __name__ == '__main__':
    preprocess_data()