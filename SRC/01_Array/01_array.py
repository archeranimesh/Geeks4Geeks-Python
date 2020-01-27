import array

# Intialize the array with signed int
arr = array.array('i',[1,2,3])


# Print the original array
print("The new created array is : ", end=" ")
for i in range(0,3):
    print(arr[i], end=" ")

print("\r")

# using append() to insert new value at the end
arr.append(4)

print("The appended array is: ", end=" ")
for i in range(0,4):
    print(arr[i], end=" ")

print("\r")


# using insert() to insert value at a specific index.
arr.insert(2,5)


print("The inserted array is: ", end=" ")
for i in range(0,5):
    print(arr[i], end=" ")

print("\r")

