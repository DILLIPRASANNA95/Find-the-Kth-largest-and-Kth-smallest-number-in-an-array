def find_kth_largest_smallest(arr, k):
    sorted_arr = sorted(arr)
    kth_largest = sorted_arr[-k]
    kth_smallest = sorted_arr[k-1]
    return kth_largest, kth_smallest

arr = [9, 4, 7, 1, 5, 2, 8, 3, 6]
k = 3

kth_largest, kth_smallest = find_kth_largest_smallest(arr, k)
print(f"Kth largest number: {kth_largest}")
print(f"Kth smallest number: {kth_smallest}")