def twoNumberSum(array, targetSum):
	hash = {}
	for i in range(len(array)):
		num = array[i]
		diff = targetSum - num
		if diff in hash:
			return [diff, num]
		else:
			hash[num] = True
	return []