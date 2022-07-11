
list1 = [10, 20, 30, 40, 50,60,70]

for i in range(len(list1)-1,-1,-1):
    print(list1[i],end=',')
print(type(list1[i]))


lst = [1,2,3,400]
res = []

for i in lst:
    # Entering elements using backward index (pos, element)
    res.insert(-i, i)

print(res)


lst = [1,2,3,400]
print(lst[::-1])

def reverse_string(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1

str = "Python Automation"
print(reverse_string(str))

