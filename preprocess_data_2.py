import pandas as pd
import demjson

def preprocess_data():

    df = pd.read_csv('vul_data_1.csv', header=None, skiprows=1)
    df.columns = ['number', '1', '2', '3', 'cve_id', 'files_changed', 'summary']
    df = df[['cve_id', 'files_changed', 'summary']]
    print(df.head(10))
    # 对于files_changes的内容json分析
    for index, item in enumerate(df['files_changed']):
        if type(item) != str:
            df = df.drop(index=[index])
            continue
        code = demjson.decode(item, "utf-8")
        name = code['filename']

        # 删除文件名不是 .c .cpp .h三个中的一个的
        if name.endswith(('.cpp', '.c', '.h', '.cc', '.cxx', '.hpp', '.c++','.C')) and ('patch' in code.keys()):
            item = code['patch']
            df.loc[index, 'files_changed'] = item
        else:
            df = df.drop(index=[index])

        # print(line)
        # 对于需要增加的部分直接放入 file_after(code['filename'])
    df.to_csv("vul_data_2.csv")
    # 对于这样的部分直接删除 \\n-\\t 直到下一个 \\n 放入file_before


if __name__ == '__main__':
    preprocess_data()