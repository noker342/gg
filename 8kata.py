length = int(input())
width = int(input())
if length == width:
    area = width * width
    print(area)
if length != width:
    perimeter = length * 2 + width * 2
    print(perimeter)
