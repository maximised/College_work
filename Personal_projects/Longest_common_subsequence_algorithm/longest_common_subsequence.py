def lcs_table(str1, str2):
	n = len(str1)
	m = len(str2)
	L = [[0]*(m+1) for i in range(n+1)]

	for i in range(n):
		for j in range(m):
			if str1[i]==str2[j]:
				L[i+1][j+1] = 1 + L[i][j]
			else:
				L[i+1][j+1] = max( L[i+1][j], L[i][j+1] )

	return L,n,m


def lcs(str1, str2):
	L,n,m = lcs_table(str1, str2)
	i = n
	j = m

	seq = [' '] * L[n][m]
	while L[i][j] > 0:
		if L[i-1][j] < L[i][j] and L[i][j-1] < L[i][j]:
			i = i-1
			j = j-1
			seq[L[i][j]] = str1[j]
		elif L[i-1][j] == L[i][j]:
			i -= 1
		else:
			j -= 1

	print(L[n][m], ':', end=' ')
	for x in seq:
		print(x, end=' ')


lcs("substinence", "conscience")
