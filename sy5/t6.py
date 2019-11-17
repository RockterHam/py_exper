import os
import re
def isExist(dictionary):
    resall = list()
    allfile = os.listdir(dictionary)
    for line in allfile:
        filepath = os.path.join(dictionary, line)
        if os.path.isdir(filepath):
            isExist(filepath)
        else:
            resall.append(line)
    return resall
if __name__ == '__main__':
    s = input()
    dictionary = s.split()[0]
    filename = s.split()[1]
    res = isExist(dictionary)
    if filename in res:
        print('true')
    else:
        print('false')
