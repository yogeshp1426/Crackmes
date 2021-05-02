import sys


input1 = sys.argv[1]
name = len(input1)

if name % 2 != 0:
	v3 = (name - 1)
	if 2 < (name - 1):
		v3 = ((ord(input1[2]))*(int('0x240e',16))/2)+1
else:
	name = (name - 1)*(int('0x9d9fd',16))
	if name < 0:
		name += 3
	v3 = ((name/4)*(int('0xd',16)))/7

print('Name:'+input1)
print('Serial:'+str(v3))
