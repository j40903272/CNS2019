param = dict()
for line in open("parameters", 'r'):
	if line == '\n':
		continue
	a, b = line.split('=')
	a = a.strip()
	b = b.strip()
	param[a] = int(b)


p = param['p']
g = param['g']
A = param['A']
B = param['B']
cipher = param['cipher']

x = (p-1)//691829
g2 = pow(g, x, p)
cnt = 0
for i in range(691829):
	tmp = pow(g2, i, p)
	if tmp == B:
		b = i
		cnt += 1
		print ('b : ', i)
	elif tmp == A:
		a = i
		print ('a : ', i)
		cnt += 1
	if cnt == 2:
		break

s_inv = pow(g2, (691829-x*a*b)%691829, p)
m = (cipher*s_inv)%p
print hex(m)[2:-1].decode('hex')
