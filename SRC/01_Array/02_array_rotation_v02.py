# Python program to rotate an array by d elements in place


def left_rotate(arr, k, n):
    print("k = ", k, " n: ", n)
    no_of_sets = gcd(n, k)
    print("left_rotate():: no_of_sets: ", no_of_sets);
    for i in range(no_of_sets):
        print("left_rotate():: i:: ", i)
        temp = arr[i]
        j = i
        while 1:
            d = (j + k) % n
            print("\t\tleft_rotate():: d= ", d, " j: ", j, " k: ",k);
            print_array(arr, n)
            arr[j] = arr[d]
            if d == i:
                break
            j = j + no_of_sets
        arr[j] = temp
        print_array(arr, n)
        print("\n")

def array_rotate(arr, n, k):
    d = -1
    i = 0
    temp = 0
    j = 0

    for i in range(gcd(n,k)):
        j = i
        temp = arr[i]
        while 1:
            d = (j + k) % n
            if d == i:
                break
            arr[j] = arr[d]
            j = d
        arr[j] = temp


def print_array(arr, size):
    for i in range(size):
        print("%d" %arr[i], end=" ")

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
k = 3
left_rotate(arr, k, n)
print_array(arr, n)
print("\n")
arr_1 = [1,2,3,4,5,6,7]
n = len(arr_1)
k = 2
left_rotate(arr_1,k,n)
print_array(arr_1,n)
print("\n")
arr_2 = [1,2,3,4,5,6,7]
n = len(arr_1)
k = 2
print("\n")
print_array(arr_2,n)
array_rotate(arr_2, n, k)
print("\n")
print_array(arr_2,n)
print("\n")
