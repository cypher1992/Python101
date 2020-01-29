# While Loop Structure


list = [1,2,5,6,3,25,6,37,6,5,7,578,9,7765,0,66,6,574,57,56,85,64,653]
position = 0
sum = 0

while position < len(list):
    sum += list[position]
    print("Sum: %s , Index: %s" % (sum, list[position]))
    position += 1

print(sum)