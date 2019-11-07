height = 100
distance = 0
for i in range(0, 10):
    distance += height
    height = height/2
    if i < 9:
        distance += height
print(height)
print(distance)
