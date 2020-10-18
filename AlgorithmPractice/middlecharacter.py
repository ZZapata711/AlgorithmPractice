# You are going to be given a word.
# Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.


def get_middle(s):
    # Test if has length 1
    if len(s) == 1:
        return s
    # Test if has even or odd length
    if len(s) % 2 == 0:
        return even_middle(s)
    else:
        return odd_middle(s)


def even_middle(s):
    return s[int(len(s)/2)-1] + s[int(len(s)/2)]


def odd_middle(s):
    return s[int((len(s)-1)/2)]

    
print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
