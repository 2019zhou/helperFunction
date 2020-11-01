import pandas as pd
import re


def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " "  # note: a space and not an empty string
        else:
            return s

    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)


def preprocess_data():
    df = pd.read_csv('vul_data_2.csv', header=None, skiprows=1)
    print(df.head(5))
    df.columns = ['number', 'cve_id', 'patch', 'summary']

    for index, item in enumerate(df['patch']):
        item = comment_remover(item)
        df.loc[index, 'patch'] = item
    # 同时处理 各种不同样式的注释
    df.to_csv("vul_data_3.csv")


if __name__ == '__main__':
    preprocess_data()