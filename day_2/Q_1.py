# Write count_vowels_consonants(text) that loops through a string and returns both counts (return v, c).
# Ignore spaces and digits.\

def count_vowels_consonants(text):
    v = 0
    c = 0
    for ch in text.lower():
        if not ch.isalpha():
            continue
        if ch in "aeiou":
            v += 1
        else:
            c += 1
    return v, c

vowels, consonants = count_vowels_consonants("MY name is vishwajeet singh")
print(vowels, consonants)