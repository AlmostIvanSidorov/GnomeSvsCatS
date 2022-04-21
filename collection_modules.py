from collections import Counter, defaultdict

mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3]

print(Counter(mylist))

d = defaultdict(lambda: 3)

d['co'] = 100
print(d['co'],d['err'])
