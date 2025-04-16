string1= "This is a sample string"
wrd=string1.split()
print(wrd)
print(' '.join(wrd[::-1]))
words = [x for x in string1.split()]
# print(' '.join(words[::-1]))
# print(words)


# for i in range(len(words)):
#     print(words[len(words)-1-i], end=' ')
# print(words[::-1])

# x =[1,2,3,4,5,6,7,8,9]
# for i in range(len(x)):
#     print(x[len(x)-1-i])