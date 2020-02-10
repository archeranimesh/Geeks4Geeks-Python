# This is the same array rotation program using reversing an Array.
# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
# 2. Reversal algorithm for array rotation

# Reverse the array within the start and end index
def reverse_array(arr, start, end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def rotate_left(arr, d):
    if d == 0 :
        return
    n = len(arr)
    reverse_array(arr, 0, d - 1)
    reverse_array(arr, d, n - 1)
    reverse_array(arr, 0, n - 1)


# Print the array
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    d = 2
    print_array(arr)
#    reverse_array(arr, 0, len(arr) - 1)
    print_array(arr)
    rotate_left(arr, d)
    print_array(arr)

