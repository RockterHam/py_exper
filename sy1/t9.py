inpKey = input("请输入：");
d = {'Python': 1, 'C': 3, 'Java': 2};
if inpKey in d:
    print(d.get(inpKey));
else:
    print("您输入的键不存在!");