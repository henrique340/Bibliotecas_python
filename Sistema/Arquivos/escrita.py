import sys

temp = open('temp.txt', 'w')
for i in range(100):
  temp.write('%02d\n' % i)
temp.close()

temp = open('temp.txt', 'r')
for n in temp:
  sys.stdout.write(n)
temp.close()