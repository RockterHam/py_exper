while True:
    inp = input("请输入一个字符：")
    if (str.isdigit(inp) == True) & (str.isalpha(inp) == False):
        print("输入的为数字")
    elif (str.isdigit(inp) == False) & (str.isalpha(inp) == True):
        print("输入的为字母")
    elif str.isalnum(inp):
        print("输入的为字母与数字")
    else:
        print("输入的为其他字符")
