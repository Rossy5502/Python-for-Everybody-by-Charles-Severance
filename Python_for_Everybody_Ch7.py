#Exercise 1, page 95
#a2=input('Enter a file name: ')
#a=open(a2,'r')
#b=a.read()
#print(b.upper())


#Exercise 2, page 95
#import statistics
#a2=input('Enter the file name: ')
#a=open(a2)
#c=[]
#for line in a:
#    if line.startswith('X-DSPAM-Confidence'):
#        b=line[19:26]
#        b2=float(b)
#        c.append(b2)
#        d=statistics.mean(c)
#print('Average spam confidence: ',d)


#Exercise 3, page 96
a2=input('Enter the file name: ')
if a2 == 'mbox.txt':
    a = open(a2)
    count = 0
    for line in a:
        if line.startswith('X-DSPAM-Confidence'):
            count=count+1
    print('There were {} subject lines in mbox.txt'.format(count))

elif a2 == 'missing.tyxt':
    print('File cannot be opened: ',a2)

elif a2 == 'na na boo boo':
    print(a2.upper(),'- You have been punk\'d!')

