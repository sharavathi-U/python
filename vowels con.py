#option 1
'''ch=input("enter a character:")
if ch.lower() in 'aeiou':
    print("vowels")
else:
    print("consoant")'''

#option 2

text='Rocking star Yash ..!!!'  #str=input("enter a text:")

vowels=0
consonants=0

for i in text.lower():
    if i.isalpha():
        if i in "aeiou":
            vowels +=1
        else:
            consonants += 1
print("vowels",vowels)
print("consonants:",consonants)


