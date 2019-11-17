import re
x='Repeat it it.'
pattern=re.compile(r'(?P<f>\b\w+\b)\s(?P=f)')
matchResult=pattern.search(x)
x=x.replace(matchResult. group(0), matchResult. group(1))
print(x)
