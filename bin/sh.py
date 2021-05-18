import shlex, subprocess as sp, os, os.path as path
from socket import gethostname

hostname = gethostname()
search = ["/home/runner/RuralSociableSpyware/bin/", "/home/runner/RuralSociableSpyware/boot/bin/"]

while True:
  cmdline = shlex.split(input(f"{os.environ['RSSUSER']}@{hostname}:{os.getcwd().replace('/home/runner/RuralSociableSpyware', '')} $").strip())
  argv0 = cmdline[0].strip() + '.py'
  print(argv0)
#  if '/' not in argv0:
#    for p in hostname:
#      np = path.join(p, argv0)
#      if path.exists(np):
#        argv0 = np
#        break
#    else:
#      print("Unknown command.")
#      continue
#  if not path.exists(argv0):
#    print("File does not exist.")
#    continue
  sp.call(["python", argv0, cmdline[1:]])