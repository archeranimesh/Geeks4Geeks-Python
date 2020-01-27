import array

arr = array.array('i', [1,2,3,1,2,5])

# printing the original array
print ("Original array : ",end="")
for i in range(0, 6):
    print(arr[i], end=" ")
print("\r")

# using index() to print first index of 1st occ of 2
print(arr.index(2))

# using reverse() to reverse the array
arr.reverse()


# printing the reverse array
print ("The array after reversing is : ",end="")
for i in range(0, 6):
    print(arr[i], end=" ")
print("\r")
