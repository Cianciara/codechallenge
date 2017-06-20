myl = [4, 8, 12]

def answer(pegs):
	"""
  Takes the positions of the pegs as an argument and 
  returns the required radius of the first disk such
  that the last disk rotates at twice the rate of the
  first disk. The radius is returned in the form [a,b]
  where the radius is equal to float(a)/b.
	"""
	D = []
	for point in range(len(pegs) - 1):
		diff = pegs[point+1] - pegs[point]
		D.append(diff)
	
	for ind, val in enumerate(D):
		if (ind+1) % 2 == 0:
			D[ind] = -1*val

	sum_series = sum(D)

	if len(D) % 2 == 0:
		a = int(2*sum_series)
		b = 1
	else:
		a = 2.0 * sum_series
		b = 3.0

	GCD = gcd(a,b) 
	a,b = a/GCD, b/GCD

	r_list = []
	B_list = []
	r1 = a/b
	r_list.append(r1)

	peg = 0
	for i in range(len(pegs)-1):
		B = pegs[i] + r_list[peg]
		B_list.append(B)
		r = pegs[i+1] - B_list[peg]
		r_list.append(r)
		peg += 1

	for radius in r_list:
		if radius < 1:
			a,b = -1, -1

	if a/b < 1:
		a,b = -1, -1

	return a,b

def gcd(x, y):
	while y != 0:
		(x, y) = (y, x % y)
	return x

answer(myl)
