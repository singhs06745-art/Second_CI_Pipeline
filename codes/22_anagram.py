def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    a = input("Enter first string: ")
    b = input("Enter second string: ")

    if are_anagrams(a, b):
        print("Strings are Anagrams")
    else:
        print("Strings are not Anagrams")