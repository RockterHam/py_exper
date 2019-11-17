def sumNumber():
    num = input("输入要计算的数:")
    number = int(input("输入要计算的层数:"))
    sumNum = 0
    listNum = []
    for i in range(number):
        listNum.append(int(num*(i+1)))
    print("列数为:",listNum)
    for i in listNum:
        sumNum += i
    return sumNum
print("总和为:%d" %sumNumber())

sumNumber()