#Exercise 1, page 116
#d={}
#a = open('words.txt','r')
#for line in a:
#    b=line.split()
#    i=0
#    for str in b:
#        i=i+1
#        d[str]=i
#print(d)
#print('Writing' in d)


#Exercise 2, page 123
#a1=input('Enter a file name: ')
#a = open(a1,'r')
#lis=[]
#for line in a:
#    if line.startswith('From:'):
#        continue
#    if line.startswith('From'):
#        line=line.strip()
#        b=line.split()
#        d=b[2]
#        lis.append(d)
#dic={}
#for e in lis:
#    dic[e]= dic.get(e,0) + 1
#print(dic)


#Exercise 3, page 124
#a1 = input('Enter file name: ')
#a = open(a1,'r')
#lis=[]
#for line in a:
#    line=line.strip()
#    if line.startswith('From:'):
#        continue
#    if line.startswith('From'):
#        l = line.rsplit()
#        l=l[1]
#        lis.append(l)
#dict={}
#for t in lis:
#    dict[t] = dict.get(t,0) + 1
#print(dict)


#Exercise 4, page 124
#a = input('Enter file name: ')
#a = open(a,'r')
#lis=[]
#for line in a:
#    line=line.strip()
#    if line.startswith('From:'):
#        continue
#    if line.startswith('From'):
#        l = line.rsplit()
#        l=l[1]
#        lis.append(l)
#dict={}
#for t in lis:
#    dict[t] = dict.get(t,0) + 1
#    m = max(dict, key=dict.get)
#    m2 = max(dict.values())
#print(m,m2)


#Exercise 5, page 124
#a1 = input('Enter file name: ')
#a = open(a1,'r')
#lis=[]
#for line in a:
#    line=line.strip()
#    if line.startswith('From:'):
#        continue
#    if line.startswith('From'):
#        l = line.rsplit()
#        w=l[1]
#        e=w.find('@')
#        p=w[e+1:]
#        lis.append(p)
#dict={}
#for t in lis:
#    dict[t] = dict.get(t,0) + 1
#print(dict)
