


def hamming_distance(s1, s2):
	'''
	returns:
	pass in:
	'''
	if len(s1) != len(s2):
		raise ValueError("Hamming dist undefined for two strings of unequal length")
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
