#! encoding=utf-8

# Creation Date: 2017-04-05 11:35:31
# Created By: Heyi Tang

import json
if __name__ == "__main__":
    with open("sum.in") as fin:
        line = fin.readline()
        actions = json.loads(line)
        datas = json.loads(fin.readline())
    for action, data in zip(actions, datas):
        if action == "NumArray":
            print len(data[0])
            print " ".join(map(str,data[0]))
            print len(datas)-1
        else:
            print action[:1], " ".join(map(str,data))
