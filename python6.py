x='hello'
rev=''
for ch in x :
    rev=ch+rev
print (rev)

#duplicate char remove
z='hello'
op=''
for ch in z:
    if ch not in op:
        op+=ch
        
    print (op)


# counting words
a='i like python programming'
print(a)
words=a.split()
print(words)
print(len(a))
print(len(words))


#counting words
str1='python_is_easy_to_learn'
words=str1.split('_')
print(words)
print(len(words))


#find largest word in string
str2='python is interpreted language'
words=str2.split()
largestWord=""
for a in words:
    if len(a)>len(largestWord):
        largestWord=a
print(largestWord)


#counting letters
str3='hello'
freq={}
for ch in str3:
    print(ch)
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)


