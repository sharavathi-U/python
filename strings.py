str="welcome to python programming"
print(str)
print(str[2:15])
print(str[2:15:2])
print(str[:15])
print(str[2:])
print(str[::-1])#reverse of a string

str="bitm bellary"
print(str)
print(str.upper())
print(str.lower())
print(str[1])
print(str[2])
print(str[5])
print(str.format())
print(str.find("bitm"))
print(str.find("bellay"))
print(str.capitalize())
print(str.casefold())
print(str.center(1))
print(str.count('b'))
print(str.isalnum())
print(str.endswith("bitm"))
print(str.format_map(0))
print(str.isalpha())
print(str.isidentifier())
str='Hello how are you'
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in str:
    if char.isalpha():   # Check only letters
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
str='Ballari institute of technology and management'
print(str)
print(str[7:18])
print(str[21:31])
print(str[15:])
print(str[:31])
print(str[2:15:2])
print(str[2:15])
print(str[7])
print(str[18])
print(str[10:4:-1])
print(str[-2])
print(str[1: :2])
print(str[0: :2])