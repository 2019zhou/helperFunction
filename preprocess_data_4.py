import pandas as pd


def preprocess_data():
    # File: readline-example-5.py
    source = open("vul_buggy.csv", "w", encoding="utf8")
    target = open("vul_repaired.csv", "w", encoding="utf8")
    file = open("vul_data_3.csv", encoding="utf8")
    for line in file:
        if line[0] == '-':
            source.write(line[1:])
        elif line[0] == '+':
            target.write(line[1:])
        elif len(line) != 0 and len(line)!= 1 and line != " "and line[0] != "#" and line[0:1] != " #":
            source.write(line)
            target.write(line)


    # df = pd.read_csv('vul_data_3.csv', header=None, skiprows=1)
    # df.columns = ['number', 'cve_id', 'patch', 'summary']
    #
    #
    # df.to_csv("vul_data_4")


if __name__ == '__main__':
    preprocess_data()
