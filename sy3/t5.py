tmpStr = input('请输入由数字与字母组成的密码字符串：')
xalphaNum=0
dalphaNum=0
numbers=0
spaceNum=0
otherNum=0
t=0
k=0
j=0
for i in tmpStr:
    if i.isalpha():
        if i.islower():
             t=1
             xalphaNum +=1
        else :
             k=1
             dalphaNum += 1
    elif i.isnumeric():
        j=1
        numbers +=1
s=xalphaNum+dalphaNum+numbers
if s>7:
    print("level is %d"%(t+j+k+1))
else :
    print("level is %d" %(t+j +k))
