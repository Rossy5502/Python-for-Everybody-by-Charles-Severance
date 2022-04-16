#Exercise 1, page 107
#a = [1, 'abc', 2, 'def']
#def chop(lis):
#    a2 = lis.remove(lis[0])
#    a2=lis.remove(lis[len(lis)-1])
#    return a2
#print(chop(a))
#print(a)

#a2 = [1, 'abc', 2, 'def']
#def middle(lis2):
#    b=lis2[1:len(lis2)-1]
#    return b
#print(middle(a2))


#Exercise 3, page 111
#fhand = open('mbox-short.txt')
#for line in fhand:
#    words = line.split()
#    #print('Debug',words)
#    if len(words) == 0 or words[0] != 'From':
#        continue
#    print(words[2])


#Exercise 4, page 111
#uni=[]
#a = open('romeo.txt','r')
#for line in a:
#    b=line.split()
#    for words in b:
#        if words in uni:
#            continue
#        uni.append(words)
#print(sorted(uni))


#Exercise 5, page 112
#a1=input('Enter a file name: ')
#a = open(a1,'r')
#count=0
#for line in a:
#    if line.startswith('From:'):
#        continue
#    if line.startswith('From'):
#        b=line.split()
#        print(b[1])
#        count=count+1
#print('There were {} lines in the file with From as the first word'.format(count))


#Exercise 6, page 112
add=[]
while True:
    a=input('Enter a number: ')
    if a == 'done':
        c=float(max(add))
        d=float(min(add))
        print('Maximum: {}'.format(c))
        print('Minimum: {}'.format(d))
        #print(add)
        break
    float(a)
    add.append(a)





