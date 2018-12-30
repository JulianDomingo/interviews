# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
#
# Do this faster than the naive method of repeated multiplication.
#
# For example, pow(2, 10) should return 1024.
def pow(base, exp):
	# Worst case scenario is where there's a very large number as the exponent.
	# We'll want to minimize this by reducing the size of the exponent until it's 1.
	# We know that halving the exponent will result in squaring the current base,
	# so it reduces down to O(N) time complexity.
	#
	# Ex.: 1^64 = 1, N = 64
	# Brute force = O(64) = O(1^N)
	# Optimal	  = O(6) = O(1(2^6))
	#
	# When we encounter an odd, we update the result with the current base. Otherwise,
	# we square the current base.
	# 2^5 => (res, base, exp) => (2, 4, 2) => (2, 16, 1) => (32, 16, 0)

	# If negative exponent, we simply just need to inverse the base.
	if exp < 0:
		base = (1.0 / base)
		exp *= -1

	res = 1.0

	while exp:
		if exp & 1:
			res *= base

		base *= base
		exp >>= 1

	return res


print(pow(2, 5))
print(pow(2, -5))
