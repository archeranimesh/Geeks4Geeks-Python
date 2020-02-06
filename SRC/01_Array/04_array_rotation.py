# Program to cyclically rotate an array by one

def rotate(arr):
    n = len(arr)
    temp = arr[n - 1]
    for x in range(n-1, 0, -1):
        arr[x] = arr[x - 1]
    arr[0] = temp

def another_rotate(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

# Print the array
def print_array(arr, msg="The array is ="):
    print(msg, end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print_array(arr)
    rotate(arr)
    print_array(arr, msg="The rotated array is =")
    arr = [1,2,3,4,5]
    another_rotate(arr)
    print_array(arr, msg="The another rotated arrar is =")



