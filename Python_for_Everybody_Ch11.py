#Exercise 2, page 149
#import statistics
#a = open('mbox-short.txt','r')
#lis = []
#for line in a:
#    line = line.rstrip()
#    if line.startswith('New Revision:'):
#        line = line.rsplit()
#        lis.append(line[2])
#lis2 = []
#for r in lis:
#    r = int(r)
#    lis2.append((r))
#p = statistics.mean(lis2)
#print('New Revision: ' + str(p))

#2nd part of Exercise 2, page 149
#import statistics
#import re
#enter = input('Enter file:')
#a = open(enter,'r')
#lis = []
#for line in a:
#    line = line.rstrip()
#    x = re.findall('^New Revision: ([0-9.]+)', line)
#    if len(x) > 0:
#        y = ''.join(x)  # converting list into string
#        z = int(y)
#        lis.append(z)
#p = statistics.mean(lis)
#print(p)

