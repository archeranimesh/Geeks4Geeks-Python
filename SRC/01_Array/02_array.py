import array

arr = array.array("i", [1,2,3,1,5])

# print the original list
for i in range(0,5):
    print(arr[i], end=" ")
print("\n")

# use pop() to remove last element.
value = arr.pop()
print("poped value = ", value)

# print the poped array
for i in range(0,4):
    print(arr[i], end=" ")
print("\n")

# use remove() to remove a value from array
# first occurence
value = arr.remove(1)
for i in range(0,3):
    print(arr[i], end=" ")
print("\n")
