set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Common:", set1 & set2)
print("Unique to set1:", set1 - set2)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
print("Merged:", merged)

marks = {"John": 85, "Alice": 95, "Bob": 70}
print("Sorted:", dict(sorted(marks.items(), key=lambda x: x[1])))

words = "apple banana apple orange banana apple".split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("Frequency:", freq)