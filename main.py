import math
import time

def F(n):
	if n < 3:
		return 1
	res = (-1)**n * (F(n - 2) / math.factorial(2 * n))

	return res

def I(n):
	default = 1
	if n < 3:
		return default

	array = [default, default]
	res = 0
	for i in range(3, n + 1):
		calculated = (-1)**i * (array[i - 3] / math.factorial(2 * i))
		array.append(calculated)
		res = calculated

	return res

def main():
	inputVal = 10

	startTime = time.time()

	res = F(inputVal)

	endTime = time.time()

	print("Result F:", res)
	print("Time F:", endTime - startTime)

	iStartTime = time.time()

	res = I(inputVal)

	iEndTime = time.time()

	print("Result I:", res)
	print("Time I:", iEndTime - iStartTime)

if __name__ == "__main__":
	main()