import pickle, sys, base64
from getpass import getpass

if (len(sys.argv) != 2):
	print(f"\33[91mexpected 1 arguments, got {len(sys.argv)-1}")
	sys.exit(2)

f = open("etc/passwd", "rb")
p = pickle.load(f)
p[base64.b64encode(sys.argv[1].encode())] = base64.b64encode(getpass().encode())
f.close()
f = open("etc/passwd", "wb")
pickle.dump(p, f)