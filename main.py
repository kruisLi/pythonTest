import re
import codecs
import csv as csv
from enum import Enum


# 设置各个学位的正则表达式
class Degree(Enum):
    def __init__(self, data):
        self.data = re.compile(data, re.I)

    PHD = r"Doctor\sof\sPhilosophy|\bp(.)?h(.)?d\b"
    MD = r"Doctor\sof\sMedicine|\bM(.)?D(.)?\b"
    MASTER = r"MASTER(\sof\s[a-zA-Z]+)?|M(.)?S(.)?"
    BACHELOR = r"BACHELOR(\sof\s[a-zA-Z]+)?|(\bBS\b)"
    ASSOCIATE = r"Associate(\sof\s[a-zA-Z]+)?|Associate\sDegree"
    HIGH_SCHOOL = r"high\sSCHOOL"


# 判断学位
def degree_judgment(data, pat):
    result = pat.search(data)
    if result:
        return True
    return False


if __name__ == '__main__':
    List_ = []  # 数据
    res = []  # 结果
    # 读取数据
    with codecs.open('./data.csv', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f, skipinitialspace=True):
            List_.append(str(row['degree']))
    f.close()
    # 判断包含的学位
    for ele_ in List_:
        flag = False
        for degree in Degree:
            flag = degree_judgment(ele_, degree.data)
            if flag:
                res.append([ele_, degree.name])
                break
        if flag is False:
            res.append([ele_, ""])
    # 将结果写入csv
    with open("result.csv", "w", encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["String", "Degree_level"])
        for ele in res:
            writer.writerow(ele)
    csvfile.close()
