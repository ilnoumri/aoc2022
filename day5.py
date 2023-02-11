from lib import open_file
from copy import deepcopy

data = open_file("5/input.txt", strip=False)

cut = 0
for idx, elt in enumerate(data):
    if elt == "":
        cut = idx
        break
crates, rules = data[:idx-1], data[idx+1:]
crates = [crate.replace("[", "").replace("]", "") for crate in crates]
base = crates[-1].split()
stk = [[base[i]] for i in range(len(base))]
crates = crates[:-1]
crates = [crate.replace("    ", "x").replace(" ", "") for crate in crates]
for crate in reversed(crates):
    i = 0
    for elt in crate:
        if elt != "x":
            stk[i].insert(0, elt)
        i += 1
stk2 = deepcopy(stk)

def move(nb, src, dst, keep_order=False, stack=stk):
    if not keep_order:
        for i in range(nb):
            top = stack[src].pop(0)
            stack[dst].insert(0, top)
    else:
        stack[dst] = stack[src][:nb] + stack[dst]
        stack[src] = stack[src][nb:]

def get_instr(rule):
    nb, src, dst = [int(elt) for elt in rule.split() if elt.isdigit()]
    return nb,src-1,dst-1

def read_top(stack):
    res = ""
    for elt in stack:
        res += elt[0]
    return res

for rule in rules:
    nb, src, dst = get_instr(rule)
    move(nb, src, dst)
    move(nb, src, dst, keep_order=True, stack=stk2)

print(read_top(stk))
print(read_top(stk2))