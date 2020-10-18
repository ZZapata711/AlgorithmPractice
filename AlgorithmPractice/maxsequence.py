# The maximum sum sub-array problem consists in finding the maximum sum
# of a contiguous subsequence in an array or list of integers:

# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]


def maxSequence(array):
    maximum = []
    for i in range(0, len(array)):
        temp = [array[i]]
        for j in range(i+1, len(array)):
            temp.append(array[j])
            if sum(temp) > sum(maximum):
                maximum = list(temp)
    return sum(maximum)


print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))







