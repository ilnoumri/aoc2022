from lib import open_file
from collections import defaultdict

data = open_file("7/input.txt")


cache = defaultdict(int)
pwd = ""
def f_size(size, name, pwd):
    path = pwd
    while True:
        cache[path] += size
        if not path:
            break
        path = path[: path.rindex("/") if "/" in path else 0]


def cd(d, pwd):
    if d == "..":
        newpwd = pwd[: pwd.rindex("/") if "/" in pwd else 0]
    elif d == "/":
        newpwd = ""
    else:
        newpwd = f"{pwd}/{d}" if pwd else d
    return newpwd

            
for elt in data:
    cmd = elt.split()
    if cmd[0] == "$":
        if cmd[1] == "cd":
            pwd = cd(cmd[2], pwd)
    elif cmd[0].isdigit():
        f_size(int(cmd[0]), cmd[1], pwd)
res = sum(size for size in cache.values() if size <= 100000)
print(res)

disk = 70000000 - cache[""]
unused_needed = 30000000
ok = []
for size in cache.values():
    if disk + size >= unused_needed:
        ok.append(size)
res2 = min(ok)
print(res2)