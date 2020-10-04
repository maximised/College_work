import string

fil = input('type file directory and name: ')
try:
    f = open(fil)
except:
    raise
    exit()


di=dict()
for line in f.read():
	line=line.translate(line.maketrans('','',string.punctuation))
	line = line.lower()
	line = line.strip()
	for letters in line:
		di[letters]=di.get(letters, 0)+1

ls=list()

for key, val in di.items():
        ls.append((val, key))

ls.sort(reverse=True)

print(ls)
