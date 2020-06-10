def lcs_table(str1, str2):
	n = len(str1)
	m = len(str2)
	L = [[0] * (m+1) for i in range(n+1)]
	for j in range(n):
		for k in range(m):
			if str1[j] == str2[k]:
				L[j+1][k+1] = L[j][k] + 1
			else:
				L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
	return L,n,m


def print_table(L, str1, str2):
	print("   ", end="")
	for s in str2:
		print(" "+s, end="")
	print()

	str = " " + str1
	c = 0
	for row in L:
		print(str[c], end=" ")
		c += 1
		for node in row:
			print(node, end=" ")
		print()


def lcs(str1, str2):
	"""
	Finds longest common subsequence of str1 and str2.

	Worst case time complexity: O(n*m)

	:param str1: first string
	:param str2: second string
	:return: the subsequence
	"""

	L,n,m = lcs_table(str1,str2)
	print_table(L,str1,str2)
	j = n
	k = m
	seq = [''] * L[n][m]
	while L[j][k] > 0:
		if L[j-1][k] < L[j][k] and L[j][k-1] < L[j][k]:
			j = j-1
			k = k-1
			seq[L[j][k]] = str1[j]
		elif L[j-1][k] == L[j][k]:
			j = j-1
		else:
			k = k-1
	print(L[n][m], ':', end=' ')
	for x in seq:
		print(x, end=' ')

######################################################
# Test code

lcs("substinence", "subzero")
