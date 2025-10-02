def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = c_count = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

s = input("Enter a string: ")
v, c = count_vowels_consonants(s)
print("Vowels:", v, "Consonants:", c)
