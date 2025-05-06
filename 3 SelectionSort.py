def selection_sort(arr):
    for i in range(len(arr)):                     # Outer loop: for each position i
        min_idx = i                                # Assume current i is the minimum
        for j in range(i+1, len(arr)):             # Inner loop: look for smaller element
            if arr[j] < arr[min_idx]:              # If found smaller, update min_idx
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap smallest element to position i
    return arr

my_list = [45, 12, 78, 3, 29]
sorted_list = selection_sort(my_list)
print("Sorted List:", sorted_list)
