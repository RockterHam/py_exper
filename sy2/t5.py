while True:
    x = input("输入x:")
    y = input("输入y:")
    x = int(x)
    y = int(y)
    if (x == 0) & (y == 0):
        print("原点")
    elif x > 0:
        if y > 0:
            print("第一象限")
        elif y < 0:
            print("第二象限")
        elif y == 0:
            print("x轴")
    elif x < 0:
        if y > 0:
            print("第四象限")
        elif y < 0:
            print("第三象限")
        elif y == 0:
            print("x轴")
    elif x == 0:
        print("y轴")