#exercise 1, page 75
#s = input('Enter a string: ')
#string = str(s)
#i=-1
#while i>-len(string)-1:
#    print(string[i])
#    i=i-1


#exercise 3, page 76
#def count(string,let):
#    word = string
#    count = 0
#    for letter in word:
#        if letter == let:
#            count = count + 1
#    print(count)
#count('pineapple','p')


#exercise 4, page 80
#a='banana'
#print(a.count('a'))


#exercise 5, page 83
#str = 'X-DSPAM-Confidence:0.8475'
#print(str.find('0'))
#print(str.find('5',19))
#floatn=str[19:25]
#print(floatn)
#print(type(floatn))
#str2=float(floatn)
#print(type(str2))


str = 'X-DSPAM-Confidence:0.8475'
print(str.replace('0.84','abc'))