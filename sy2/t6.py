import random

RND1 = random.randint(0, 100)
RND2 = random.randint(0, 100)

if RND1 > RND2:
    temp = RND2
else:
    temp = RND1
for i in range(temp, 0, -1):
    num = i
    if (RND1%i == 0) & (RND2%i == 0):
        break
max = num
min = (RND1 * RND2)/num
print('RN1：{0}\nRN2：{1}'.format(RND1,RND2))
print('最大公约数：%d'%max)
print('最小公倍数：%d'%min)