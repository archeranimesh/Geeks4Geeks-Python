arr = [1,2,3,4,5,6,7]

n = len(arr)
d = 3

print("n = ", n, "d = ", d)
new_arr = arr[0:d]
print(new_arr)
arr = arr[d:]
arr.extend(new_arr)
print(arr)
