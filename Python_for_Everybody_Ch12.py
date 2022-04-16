#Exercise 1, page 164
#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#try:
#    b = input('Type your URL: ')
#    if b == 'http://data.pr4e.org/romeo.txt':
#        pass
#    else:
#        exit()
#except:
#    print('The URL entered is incorrect!')
#    exit()
#cmd = 'GET ' + b + ' HTTP/1.0\r\n\r\n'
#cmd2 = cmd.encode()
#spl = b.split('/')
#mysock.connect((spl[2], 80))
#mysock.send(cmd2)
#while True:
#    data = mysock.recv(512)
#    if len(data) < 1:
#        break
#    print(data.decode(),end='')
#mysock.close()


#Exercise 3, page 164
#import urllib.request
#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#size = 0
#for line in fhand:
#    a = line.decode().strip()
#    print(a)
#    size = size + len(a)
#if size > 3000:
#    print('The max number of characters allowed is 3000.')
#else:
#    print("\nThere are {} number of characters".format(size))


#Exercise 4, page 164
#import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
#import ssl

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

#tags = soup('p')
#a = 0
#for tag in tags:
#    a = a + 1
#print(a)


