# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on
# their places.

# Zero isn't an odd number and you don't need to move it.
# If you have an empty array, you need to return it.


def sort_array(source_array):
    # Separate list into two lists of evens and odds
    evens = []
    odds = []
    for i in source_array:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    # Sort odds list
    odds.sort()
    # Check if a given item is in evens list.
    # If it is, we append it first, otherwise we append next item in evens list
    sorted_array = []
    j = 0
    for i in source_array:
        if i in evens:
            sorted_array.append(i)
        else:
            sorted_array.append(odds[j])
            j += 1
    # Return a sorted array.
    return sorted_array


print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 1, 8, 0]))
