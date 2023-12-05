#1
"""def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
s1 = input("please enter your first string value: ")
s2 = input("please enter your second string value: ")
check(s1, s2)"""
#2
"""
def anagrams(inp1: str, inp2: str) -> bool:
  # if the length of the two strings is not the same, they are not anagrams.
  if len(inp1) != len(inp2):
      return False
  counts = {}
  for c1, c2 in zip(inp1, inp2):
    if c1 in counts.keys():
      counts[c1] += 1
    else:
      counts[c1] = 1
    if c2 in counts.keys():
      counts[c2] -= 1
    else:
      counts[c2] = -1
  for count in counts.values():
    if count != 0:
      return False
  return True
def main():
  inp1 = input("enter your first string")
  inp2 = input("enter your second string")
  if anagrams(inp1, inp2):
    print(f"{inp1} and {inp2} are anagrams")
  else:
    print(f"{inp1} and {inp2} are not anagrams")
if __name__ == "__main__": 
  main()"""
#3
from collections import Counter
def check(s1, s2):
    if(Counter(s1) == Counter(s2)):
        print("The two strings are anagram of each other")
    else:
        print("The two strings are not anagram of each other")
s1 = input("enter your first string")
s2 = input("enter your second string")
check(s1, s2)
