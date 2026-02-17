# Enumeration Example with  List
fruits = ["Apple", "Banana", "Kiwi", "Cherry"]
for i, name in enumerate(fruits, start = 1):
    print(i, name)

# Enumeration of Character
word = "Satheesh"
for i, ch in enumerate(word, start = 0):
    print(i, ch)

# Enumeration through Tuples
fruits = {"Orange", "Cherry", "Kiwi"}
for i, name in enumerate(fruits, start = 1):
    print(i ,name)

# Enumerate through the TestCases
Test_cases = ["Login", "DashBoard", "Custom"]
for i, case_no in enumerate(Test_cases, start = 1):
    print("Excuting the Test Cases", i ,": " ,case_no)

# Accessing of the Scenario
a = ["God", "is", "Great"]
b = enumerate(a)
nxt_val = next(b)
print(nxt_val)
print(nxt_val)

#Duplicate detection using Enumeration
characters = ["Krillin", "Goku", "Gohan", "Piccolo",
              "Krillin", "Goku", "Vegeta", "Gohan", "Piccolo",
              "Piccolo", "Goku", "Vegeta", "Goku", "Piccolo"]

character_map = {character: [] for character in set(characters)}

for i, character in enumerate(characters):

    character_map[character].append(i)
    print(character_map)

print(enumerate(['a', 'b']))
