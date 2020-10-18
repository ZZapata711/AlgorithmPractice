# Write a program that finds the next integral perfect square after the given perfect square
# If the given number is not a perfect square, return -1
import numpy as np


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if np.sqrt(sq).is_integer():
        while True:
            sq = sq + 1
            if np.sqrt(sq).is_integer():
                return sq
                break
            else:
                continue
    else:
        return -1


print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(319225))
print(find_next_square(15241383936))

print(find_next_square(155))
print(find_next_square(342786627))
