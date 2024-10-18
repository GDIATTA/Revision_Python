vec1 =[];
#thislist = list({"apple", "banana", "cherry"}) # note the double round-brackets
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
for fruit in thislist:
    print("Fruit " + fruit)
vec1.append(0);
vec1.append(1);
thislist1 = ["apple", "banana", "cherry"]
thislist1.insert(2, "watermelon")
print(thislist1)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist.remove("banana");
print(thislist)
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)
thislist.clear()
print(thislist)

thislist2 = ["apple", "banana", "cherry"]
y=[x for x in thislist2]
print(y)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print(vec1);