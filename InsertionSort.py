def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

input_list = input("Enter a list of numbers separated by spaces: ").split()

insertion_sort(input_list)
print("Sorted list:", input_list)
