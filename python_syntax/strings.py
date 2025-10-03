# Strings are similar to arrays
s = "abc"
print(s[0:2])  # this gives ab

# But they are immutable
s[0] = "A"

# So this creates a new string
s += "def"
print(s)  # this gives abcdef but its a new string (new space in memory)

"""
s = "abc"
Memory: s points to ┌─────┐
                    │"abc"│ at address 0x1000
                    └─────┘

s += "def"
Memory: s NOW points to ┌────────┐
                        │"abcdef"│ at address 0x2000 (NEW!)
                        └────────┘
       
       The old "abc" at 0x1000 still exists (until garbage collected)
"""

# In the rare cases you may need the ASCII value
# of a char
print(ord("a"))  # gives 97
print(ord("b"))  # gives 98

# COmbine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))  # this gives abcdef
