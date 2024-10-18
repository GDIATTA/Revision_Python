fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = []
#for x in fruits:
#  if "a" in x:
#    newlist.append(x)
#print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
#thislist = [100, 50, 65, 82, 23]
#thislist.sort(reverse = True)
#print(thislist)

#def myfunc(n):
#  return abs(n - 50)

#thislist = [100, 50, 65, 82, 23]
#thislist.sort(key = myfunc)
#print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)