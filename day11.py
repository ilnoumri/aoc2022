from lib import open_file
from math import prod
from functools import lru_cache
from operator import add, mul

data = open_file("11/input.txt")

monkeys = []
monkey = []
for elt in data:
    if not elt:
        monkeys.append(monkey)
        monkey = []
    else:
        monkey.append(elt)
if monkey:
    monkeys.append(monkey)

def get_monks():
    common_mod = 1
    monk = {}
    monk_inspect = {}
    for monkey in monkeys:
        idx = int(monkey[0].replace(":", "").split()[1])
        monk[idx] = {}
        monk_inspect[idx] = 0
        starting = monkey[1].replace(",", "").split()[2:]
        monk[idx]["starting"] = [int(elt) for elt in starting]
        monk[idx]["divisible"] = int(monkey[3].split()[-1])
        monk[idx][True] = int(monkey[4].split()[-1])
        monk[idx][False] = int(monkey[5].split()[-1])
        if "+" in monkey[2]:
            monk[idx]["op"] = add
            arg = monkey[2].replace("=", "+").split("+")[-1].lstrip()
            if arg.isdigit():
                arg = int(arg)
            monk[idx]["arg"] = arg
        elif "*" in monkey[2]:
            monk[idx]["op"] = mul
            arg = monkey[2].replace("=", "*").split("*")[-1].lstrip()
            if arg.isdigit():
                arg = int(arg) 
            monk[idx]["arg"] = arg
        common_mod *= monk[idx]["divisible"]
    return monk, monk_inspect, common_mod


def round(n, divby3=True):
    monk, monk_inspect, common_mod = get_monks()
    for i in range(n):
        for k, v in monk.items():
            while (v["starting"] and (inspect := v["starting"].pop())):
                monk_inspect[k] += 1
                op = v["op"]
                res = op(inspect, v["arg"] if v["arg"] != "old" else inspect)
                if divby3:
                    res //= 3
                else:
                    res %= common_mod
                condition = (res % v["divisible"]) == 0
                monkey = v[condition]
                monk[monkey]["starting"].append(res)
    return monk_inspect

monk_inspect = round(20)
res = prod(sorted(monk_inspect.values(), reverse=True)[:2])
print(res)

monk_inspect2 = round(10000, False)
res2 = prod(sorted(monk_inspect2.values(), reverse=True)[:2])
print(res2)
