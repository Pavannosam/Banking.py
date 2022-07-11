
'''Sorting a List by user defined input values '''


l = []
n = int(input('Enter list : '))
for i in range(0,n):
    ele = int(input())
    l.append(ele)
print(l)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
print(l)

strng = "Hey Hi i'm Python AUtomation Tester"
words = strng.split()
words.sort()
print(words)
print(type(words))
for word in words:
    print(word)