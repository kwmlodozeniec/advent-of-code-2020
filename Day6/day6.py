data = []
with open("6.data", "r") as f:
    data = [len(set(line.replace("\n", ""))) for line in f.read().split("\n\n")]

print(f"Sums: {sum(data)}")

data = open("6.data").read().split("\n\n")

total = 0
for entry in data:
    items = entry.split()
    common = set.intersection(*map(set, items))
    total += len(common)
print(f"Total: {total}")
