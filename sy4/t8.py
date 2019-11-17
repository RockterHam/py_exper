import re
x=" i like milk , my name is mike."
pattern=re.compile(r'(?:[^\w]|\b)i(?:[^\w])')
while True:
    result=pattern. search(x)
    if result:
        if result.start(0)!=0:
            x=x[: result.start(0)+1]+'I'+x[ result. end(0)-1:]
        else: x=x[: result.start(0)]+'I'+x[ result. end(0)-1:]
    else:
        break
print(x)
