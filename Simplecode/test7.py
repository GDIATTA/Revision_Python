#thisset = {"apple", "banana", "cherry", "apple", True,1,2}
#print(thisset)

#thisset = {"apple", "banana", "cherry"}
#thisset.add("orange")
#print(thisset)

#thisset = {"apple", "banana", "cherry"}
#tropical = {"pineapple", "mango", "papaya"}
#thisset.update(tropical)
#print(thisset)

#thisset = {"apple", "banana", "cherry"}
#mylist = ["kiwi", "orange"]
#thisset.update(mylist)
#print(thisset)

#thisset = {"apple", "banana", "cherry"}
#thisset.remove("banana")
#thisset.discard("banana")
#x = thisset.pop()
#thisset.clear()
#del thisset
#print(thisset)

#thisset = {"apple", "banana", "cherry"}
#del thisset
#print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
set1.intersection_update(set2)
print(set1)
print(set3)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

print(set({
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}))

print(set((1,2,3)))
