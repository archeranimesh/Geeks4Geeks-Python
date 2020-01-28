arr = [1,2,3,4,5,6,7]

n = len(arr)
d = 3

def leftRotate(arr, d, n):
    return (arr[d:] + arr[0:d])

print("n = ", n, "d = ", d)

print(leftRotate(arr, d, n))
