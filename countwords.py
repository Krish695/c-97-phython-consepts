name=input("Hello what is your name")
print("Hi",name)
chcount=0
wordcount=0
for i in name:
    chcount=chcount+1
    if (i==''):
        wordcount=wordcount+1
print("num of words:")
print(wordcount)
print(chcount)
