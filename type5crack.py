
try:
	from passlib.hash import md5_crypt
	import sys, time
except:
	print("""
	 **************************************************
	*This program requires passlib.hash, sys, and time.*
	*Ensure they are installed and try again. (use pip)*
	 **************************************************
	 """)
	exit()
if len(sys.argv)<3:
	print("""
	 **************************************************
	*This program requires two arguments.  The first is*
	*the cisco type 5 password (salted md5) you wish to*
	*crack. The second is the path to a wordlist to try*
	 **************************************************
	""")
	exit()
	
hash = sys.argv[1]
dict = []

with open(sys.argv[2], 'r') as wordlist:
	count = 1
	try:
		for i in wordlist:
			try:
				dict.append(i.rstrip('\n'))
			except:
				print("Unrecognized word # "+count)
				count+=1
	except Exception as e:
		print("""
		 **************************************************
		*An error occured processing your word list. Some  *
		*of the words were ingested, but the process exited*
		*Because of an unrecognized character. See error e *
		 **************************************************
		"""+str(e))
print(str(len(dict))+" passwords ingested. Beginning crack")
	
for password in dict:
	if md5_crypt.verify(password, hash):
		print(sys.argv[1]+":"+password)
		exit()

print("Password not found. Try another dictionary file")