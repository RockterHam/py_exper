def lamdba(x):
    x=x*x
    return  x
app_list = [1, 2, 3]
s=0
for i in range(len(app_list)):
    s=s+lamdba(app_list[i])
print(s)
