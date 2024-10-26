
variable1 = (input("Enter a list of numbers separated by spaces: "))
list1 = (variable1.split())
for i in range(len(list1)):
    list1[i] = int(list1[i])

list1.sort()
#print(list1)
print(f"AVG: {sum(list1)/len(list1)}")
print(f"Sum: {sum(list1)}")
print(f"Min: {list1[0]}")
print(f"Max: {list1[-1]}")
print(f"")

