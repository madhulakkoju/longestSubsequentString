s=input("enter string")
l=[]
n=int(input("how many ?"))
for i in range(n):
	l.append(str(input()))
c=[]
c.append(s[0])
j=1
f=[]
for i in range(1,len(s)):
	if(c[j-1] == s[i]):
		continue
	else:
		c.append(s[i])
		j =j+1
ch=[]
for i in range(len(c)):
	ch.append(c[i])
for i in range(len(l)):
	for j in range(i,len(l)):
		if len(l[i])<len(l[j]):
			x= l[i]
			y=l[j]
			del l[i]
			l.insert(i,y)
			del l[j]
			l.insert(j,x)
for i in range(len(l)):
	j=0
	p=0
	sp=0
	ch=[]
	for jf in range(len(c)):
		ch.append(c[jf])
	if(len(l[i])>len(s)):
		continue
	while(j<len(l[i])):
		if(l[i][j]==s[sp]):
			if(l[i][j] in ch):
				ch.remove(l[i][j])
			j=j+1
			sp=sp+1
		elif l[i][j]!=s[sp]:
			sp=sp+1
		if(sp>=len(s)):
			break
	if(j==len(l[i]) ):
		f.append((i,len(c)-len(ch)))
for i in range(len(f)):
	for j in range(i,len(f)):
		if f[i][1] < f[j][1]:
			x= f[i]
			y=f[j]
			del f[i]
			f.insert(i,y)
			del f[j]
			f.insert(j,x)
		elif f[i][1]==f[j][1]:
			if f[i][0] > f[j][0]:
				x= f[i]
				y=f[j]
				del f[i]
				f.insert(i,y)
				del f[j]
				f.insert(j,x)
print()
print(l[f[0][0]])



