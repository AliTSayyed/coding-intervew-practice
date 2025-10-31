# HashMap (aka dict)

myMap = {}
myMap["alice"] = 88  # this is how to insert
myMap["bob"] = 77
print(myMap)

# gives number of keys
print(len(myMap))

myMap["alice"] = 90  # over write key value
print(myMap["alice"])

print("alice" in myMap)  # search for a key (constant time)
myMap.pop("alice")  # removes a key

myMap = {"alice": 80, "bob": 77}

# Looping through maps
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)

# good way to initilize by 1 using a default
myMap[val] = myMap.get(val, 0) + 1

for key in myMap:                    # Iterate keys
for value in myMap.values():         # Iterate values
for key, value in myMap.items():     # Iterate key-value pairs
for key in sorted(myMap):            # Iterate keys in sorted order
for key in sorted(myMap.keys()):     # Same as above

# Use dict1.items() <= dict2.items() for subset checking
