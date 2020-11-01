import pandas as pd
import demjson


def preprocess_data():
    # 读入数据
    df = pd.read_csv('vul_data.csv', header=None, skiprows=1)
    df.columns = ["number", "authentication_required", "availability_impact", "cve_id", "cve_page", "cwe_id",
                  "access_complexity",
                  "confidentiality_impact", "integrity_impact", "publish_date", "score", "summary", "update_date",
                  "vulnerability_classification", "ref_link", "commit_id", "commit_message", "files_changed", "lang",
                  "project",
                  "version_after_fix", "version_before_fix"]
    df = df[['cve_id', 'summary', 'files_changed']]
    #file_after = []
    #file_before = []

    # 数据中有这样的 <_**next**_> 的信息全部分割
    for index, item in enumerate(df['files_changed']):
        content_str = "<_**next**_>"
        originalstr = item
        position = 0
        t = 1
        if type(originalstr) != str:
            df = df.drop(index=[index])
            continue
        p = originalstr.find(content_str, position)
        pre = p
        while t != -1 and p != -1:
            p = originalstr.find(content_str, position)
            position = p + len(content_str)
            t = originalstr.find(content_str, position)
            if t == -1:
                curStr = originalstr[position:]
            else:
                curStr = originalstr[position:t]
            df2 = pd.DataFrame([[df.loc[index, 'cve_id'], curStr, df.loc[index, 'summary']]])
            df = df.append(df2)


        if pre != -1:
            item = item[0:pre]
            df.loc[index, 'files_changed'] = item

    df.to_csv("vul_data_1.csv")



def format_str(string):
    for char in ['\r\n', '\r', '\n']:
        string = string.replace(char, ' ')
    return string


if __name__ == '__main__':
    preprocess_data()
