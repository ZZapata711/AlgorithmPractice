def duplicate_count(text):
    counter = 0
    text = list(sorted(text.lower()))
    for char in text:
        print(text)
        text.remove(char)
        if char in text:
            counter += 1
            while True:
                if char in text:
                    text.remove(char)
                else:
                    break
    return counter


# print(duplicate_count("aabcde"))
# print(duplicate_count("ABBAC"))
# print(duplicate_count("aA11"))
# print(duplicate_count("indivisibility"))
print(duplicate_count("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(duplicate_count("Indivisibilities"))


