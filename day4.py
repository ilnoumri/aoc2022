from lib import open_file

data = open_file("4/input.txt")


def get_range(section):
    a, b = section.split("-")
    return set(range(int(a), int(b) + 1))

res = 0
res2 = 0

for elt in data:
    s1, s2 = elt.split(",")
    r1, r2 = get_range(s1), get_range(s2)
    bigger, smaller = r1, r2
    if len(r2) > len(r1):
        bigger, smaller = r2, r1
    res += 1 if len(smaller - bigger) == 0 else 0
    res2 += 1 if bigger - smaller != bigger else 0

print(res)
print(res2)