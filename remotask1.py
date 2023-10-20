# def lexicographically_smallest(s: str) -> str:
#     s = list(s)  # Convert the string to a list
#     changes = 0  # Counter to keep track of the number of changes
#     for i in range(len(s)):
#         if s[i] != "a" and changes < 5:
#             s[i] = "a"
#             changes += 1
#         if changes == 5:
#             break
#     return "".join(s)  # Convert the list back to a string and return


s = "aedcba"
print(lexicographically_smallest(s))


def lexicographically_smallest(s: str) -> str:
    s = list(s.lower())  # Convert the string to a list
    changes = 0  # Counter to keep track of the number of changes
    for i in range(len(s)):
        if s[i] != "a" and changes < 5:
            s[i] = "a"
            changes += 1
        if changes == 5:
            break
    return "".join(s)  # Convert the list back to a string and return


# # s = "aedcba"
# s = "fgsergkgmdflgdfk"
# print(lexicographically_smallest(s))


def lexicographically_smallest(s: str) -> str:
    import string

    s = list(s.lower())  # Convert the string to a list in lower case form
    changes = 0  # Create a counter to keep track of the number of
    letters = string.ascii_letters[:26].lower()

    for i in range(len(s)):
        if s[i] != letters[i] and changes < 5:
            s[i] = letters[i]
            changes += 1
        if changes == 5:
            break
    return "".join(s)  # Convert the list back to a string and return


# s = "aedcba"
s = "fdgfdkgndfgjdfkgndf"
print(lexicographically_smallest(s))

# Modify the code such that no more than two instances of the same letter appear in the output.
