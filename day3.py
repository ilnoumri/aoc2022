from lib import open_file

data = open_file("3/input.txt")

def get_compart(item):
    middle = int(len(item)/2)
    return (item[:middle], item[middle:])

def common_elt(a, b, c=None):
    if not c:
        return set(a).intersection(set(b)).pop()
    return set(a).intersection(set(b)).intersection(set(c)).pop()

def get_priority(letter):
    if letter >= "a" and letter <= "z":
        return ord(letter) - 96
    return ord(letter) - 38

res = 0
for elt in data:
    a, b = get_compart(elt)
    res += get_priority(common_elt(a,b))

print(res)

res2 = 0
for i in range(0, len(data), 3):
    a, b, c = data[i], data[i+1], data[i+2]
    res2 += get_priority(common_elt(a, b, c))

print(res2)