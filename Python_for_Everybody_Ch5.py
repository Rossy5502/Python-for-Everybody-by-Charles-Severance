#Exercise 1, page 70
#lis=[]
#while True:
#    try:
#        a=input('Enter a number: ')
#        float(a)
#        lis.append(int(a))
#    except:
#        if a == 'done':
#            print(sum(lis), len(lis), float(sum(lis)/len(lis)))
#            break
#        else:
#            print('Invalid input')


#Exercise 2, page 71
lis=[]
while True:
    try:
        a=input('Enter a number: ')
        float(a)
        lis.append(int(a))
    except:
        if a == 'done':
            print(sum(lis), len(lis), max(lis), min(lis))
            break
        else:
            print('Invalid input')

