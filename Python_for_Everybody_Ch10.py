#Exercise 1, page 134
#q=input('Enter a file name: ')
#file = open(q,'r')
#lis = []
#for a in file:
#    if a.startswith('From:'): continue
#    if a.startswith('From'):
#        b = a.strip()
#        b = a.split()
#        lis.append(b)
#lis2=[]
#for b in lis:
#    lis2.append(b[1])
#dic={}
#for c in lis2:
#    dic[c] = dic.get(c,0) + 1
#lis3 = []
#for key,val in dic.items():
#    lis3.append((val,key))
#lis3.sort(reverse=True)         #built-in type
#(m,m2) = max(lis3)              #built-in function
#print(m2,m)


#Exercise 2, page 134
#q = input('Enter a file name: ')
#a = open('mbox-short.txt','r')
#lis = []
#for line in a:
#    if line.startswith('From:'): continue
#    if line.startswith('From'):
#        line = line.rstrip()
#        line = line.rsplit()
#        line = line[5]
#        line = line[0:2]
#        lis.append((line))
#dic={}
#for d in lis:
#    dic[d] = dic.get(d,0) + 1
#for key, val in dic.items():
#    print(key,val)


#Exercise 3, page 135   (write a program that reads a file and prints the letters in decreasing order......
import string
fil = open('words.txt','r')
lis = []
lis2 = []
for letter in fil:
    letter = letter.rstrip()
    letter = letter.lower()
    letter = letter.translate(letter.maketrans('', '', string.punctuation))
    letter = letter.replace(' ','')
    letter = letter.split()
    for y in letter:
        lis[:] = y
        for k in lis:
            lis2.append(k)
dic = {}
for d in lis2:
    dic[d] = dic.get(d,0) + 1
#print(sum(dic.values()))       #to sum the values in dic
lis3 =[]
for key, value in dic.items():
    p = (value/942)*100
    lis3.append((p,key))
lis3.sort(reverse=True)
print(lis3)


