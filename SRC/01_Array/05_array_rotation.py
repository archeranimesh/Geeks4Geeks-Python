# Finding element in a sorted but rotated array
# http://theoryofprogramming.com/2017/12/16/find-pivot-element-sorted-rotated-array/
# https://www.geeksforgeeks.org/python-program-for-binary-search/
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

# Geeks for Geeks Pivoted index
def geeks_find_pivot(arr, low, high, debug=False):
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high)/2)

    if debug:
        print("arr = ", arr, " low ", low, " high ", high, " mid ", mid, " arr[mid] ", arr[mid], " arr[mid + 1] ", arr[mid+1], " arr[low] ", arr[low], " arr[mid -1] ", arr[mid-1])

    if mid < high and arr[mid] > arr[mid +1]:
        return mid
    if mid > low and arr[mid] < arr[mid -1]:
        return mid -1
    if arr[low] >= arr[mid]:
        return geeks_find_pivot(arr, low, mid - 1, debug)
    return geeks_find_pivot(arr, mid + 1, high, debug)

# Geeks for Geeks Binary Search
def geeks_binary_search(arr, low, high, key):
    if high < low:
        return -1

    mid = int((low + high)/2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return geeks_binary_search(arr, (mid + 1), high, key)

    return geeks_binary_search(arr, low, (mid -1), key)

# Normal Binary Search Function.
def binary_search(arr, low, high, x, debug=False):
    if debug:
        print("arr = ", arr, " low ", low, " high ", high, " x ", x)
    if high >= low:
        mid = int(low + (high - low)/2)
        if debug:
            print("mid = ", mid, " arr[mid] ", arr[mid])
        # value is present in mid point itself
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
            if debug:
                print("high: ", high)
            return binary_search(arr, low, high, x, debug)
        else:
            low = mid + 1
            if debug:
                print("low: ", low)
            return binary_search(arr, low, high, x, debug)
    else:
        # Wrong high was passed so returning -1
        return -1

# Pivoted binary search
def geeks_pivoted_search(arr, n, key):
    pivot = geeks_find_pivot(arr, 0, n - 1)

    if pivot == -1:
        return geeks_binary_search(arr, 0, n-1, key, True)

    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return geeks_binary_search(arr, 0, pivot - 1, key, True)
    return geeks_binary_search(arr, pivot + 1, n -1, key, True)


if __name__ == "__main__":
    arr = [12,14,18,2, 3, 6,8,9]
    binary_arr = [3,6,8,9,12,14,18,21]
    x = 18
    result = binary_search(binary_arr, 0, len(binary_arr) - 1, x, True)

    if result != -1:
        print("The element is found in index ", result, " value is ", binary_arr[result], " matches with value passed ", x)
    else:
        print("The value not found")

    result = geeks_binary_search(binary_arr, 0, len(binary_arr) - 1, x)
    if result != -1:
        print("The element is found in index ", result, " value is ", binary_arr[result], " matches with value passed ", x)
    else:
        print("The value not found")

    result = geeks_find_pivot(arr, 0, len(arr) -1, True)
    print("The result for pivot is ", result)
    result = geeks_pivoted_search(arr, len(arr), x)
    if result != -1:
        print("The element is found in index ", result, " value is ", arr[result], " matches with value passed ", x)
    else:
        print("The value not found")
