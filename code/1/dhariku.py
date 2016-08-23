def testPrime(input):
	number=int(input)
	if number<=2:
		return False;
	for i in range(2, int(input**(0.5))+1):
		if number%i==0:
			return False;
	return True;

print testPrime(9);	
