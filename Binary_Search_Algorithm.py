import random
def generate_number_list(length):
    number_list = [random.randint(0, 100) for _ in range(length)]
    number_list.sort()
    for i in range(1, len(number_list)):
        number_list[i] = number_list[i - 1] + 2
    return number_list

def perform_binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid  # Return the index of the target if found
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1  # Return -1 if target is not found

# Taking input from the user and stores Length of the list in list_length ,to search for that number in search_target
list_length = int(input("Enter the number of elements in the list: "))
search_target = int(input("Enter the number to search for: "))

# Generate the list and perform binary search
number_list = generate_number_list(list_length)
search_index = perform_binary_search(number_list, search_target)

# Print the result
if search_index != -1:
    print(f"The number is in the list at index {search_index}.")
else:
    print("The number is not present in the list.")
