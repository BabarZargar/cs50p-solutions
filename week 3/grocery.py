d = {}
while True:
    try:
        item = input().upper()
        d[item] = d.get(item, 0) + 1

    except EOFError:
        break

for item in sorted(d):
    print(d[item], item)


