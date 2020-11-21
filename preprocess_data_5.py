import pandas as pd
import re


def remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " "  # note: a space and not an empty string
        else:
            return s

    pattern = re.compile(
        r'@@.*@@',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)


def preprocess_data():
    # 删除 @@ --- @@的部分同时删除所有的换行符

    for name in {"vul_data_3.csv"}:
        df = pd.read_csv(name, header=None, skiprows=1)
        df.columns = ['number', 'cve_id', 'patch', 'summary']
        print(df.head(5))
        for index, item in enumerate(df['patch']):
            item = re.sub(r'\\n', "", item)

            df.loc[index, 'patch'] = item
            print(item)
        if name == "vul_buggy.csv":
            df.to_csv("vul_buggy2.csv")
        else:
            df.to_csv("vul_repaired2.csv")


if __name__ == '__main__':
    preprocess_data()
