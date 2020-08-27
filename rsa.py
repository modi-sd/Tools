import sympy
import gmpy2
print("1.calculate n\n2.calculate p\n3.calculate q\n4.encryption with n and e\n5.calculate d\n6.decryption with n, e ,p , ct\7.decrypt with small e")
choose = int(raw_input("choose operation = "))
if choose == int(1):
	q = int(raw_input("Enter q = "))
	p = int(raw_input("Enter p = "))
	n = p * q
	totient = raw_input("Calculate totient y/n : ")
	if totient == "y": 
		totient_n = (q - 1)*(p - 1)
		print("totient(n) = "+str(totient_n))
	else:
		exit
	print("n = "+str(n))
elif choose == int(2):
	n = int(raw_input("Enter n = "))
	q = int(raw_input("Enter q = "))
	p = n / q
	if type(p) != int :
		print("Operation cannot be done")
	else :
		print("p = "+str(p))
elif choose == int(3):
	n = int(raw_input("Enter n = "))
	p = int(raw_input("Enter p = "))
	q = n / p
	if type(q) != int :
		print("Operation cannot be done")
	else :
		print("q = "+str(q))
elif choose == int(4):
        n = int(raw_input("Enter n = "))
        e = int(raw_input("Enter e = "))
        pt = int(raw_input("Enter pt = "))
	ct = (pt**e) % n
        if 1 < pt < n :
                print("ciphertext = "+str(ct))
        else :
                print("Operation cannot be done")
elif choose == int(5):
	p = int(raw_input("Enter p = "))
	q = int(raw_input("Enter q = "))
	e = int(raw_input("Enter e = "))
	L = (p-1)*(q-1)
	d = sympy.mod_inverse(e, L)
	print("decryption exponent = "+str(d))
elif choose == int(6):
	p = int(raw_input("Enter p = "))
	ct = int(raw_input("Enter ciphertext = "))
	e = int(raw_input("Enter e = "))
	n = int(raw_input("Enter n = "))
	q = n/p
	L = (p-1)*(q-1)
	d = sympy.mod_inverse(e, L)
	pt = pow(ct, d, n)
	print("plaintext is : "+str(pt))
elif choose == int(7) :
    N = int(raw_input("Enter N = "))
    e = int(raw_input("Enter e"))
    ct = int(raw_input("Enter ct = "))

    gs = gmpy2.mpz(ct)
    gm = gmpy2.mpz(N)
    ge = gmpy2.mpz(e)
    
    pt, exact = gmpy2.iroot(gs, ge)
    print format(pt, 'x').decode('hex')
else:
    exit()