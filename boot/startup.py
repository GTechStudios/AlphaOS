import random, time, subprocess as sp
print()
for i in range(35):
	print(f"\33[Floading {i}% {random.randint(450, 500)}b/s")
	time.sleep(random.random()/3)
print(f"\33[F\33[2Kloading done, starting login")
sp.call(["python", "bin/login.py"])