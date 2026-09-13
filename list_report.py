items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

more_than_four = 0
for item in items:
    if len(item) > 4:
        more_than_four += 1
print("Items with more than 4 letters:", more_than_four)

longest = ""
for item in items:
    if len(item) > len(longest):
        longest = item
print("Longest item:", longest)
