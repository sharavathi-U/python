roll_no={1:'ram',2:'venu',3:'lakshmi',4:'kumar',5:'thomas'}
print(roll_no)

roll_no[1]='shayam'
print(roll_no)
print(roll_no.values())
print(roll_no.keys())

s='the cow the dog the cat the cow'
l=s.split()
print(l)

d={}
for word in l:
    d[word]=d.get(word,0)+1
print(d)
print("-------------------------------------")
str='programming'
d={}

for ch in str:
    d[ch]=d.get(ch,0)+1