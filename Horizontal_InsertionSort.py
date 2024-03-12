def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

input_list = input("Enter a list of numbers separated by spaces: ").split()

print("Unsorted List: ", input_list)

insertion_sort(input_list)

print("Sorted list:", end=" ")
for item in input_list:
    print(item, end=" ")
