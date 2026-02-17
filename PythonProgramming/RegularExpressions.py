## A Regular Expression (Regex) is a pattern used
# to search, match, or manipulate text.

# Python provides the re module for regex
"""
Function	Purpose
re.search()	Finds first match
re.match()	Matches from beginning
re.findall()	Returns all matches
re.sub()	Replace pattern
re.split()	Split string
re.compile()	Compile pattern

Pattern	Meaning
.	Any character
\d	Digit
\D	Non-digit
\w	Word character
\W	Non-word character
\s	Whitespace
^	Start of string
$	End of string
*	0 or more
+	1 or more
?	0 or 1
{n}	Exactly n times
"""

import re

# re.search
text = "My phone number is 9876543210"

result = re.search(r"\d+", text)
print(result.group())

# re.findAll
text = "Order 123, item 456"
print(re.findall(r"\d+", text))

# re.match
email = "test@gmail.com"

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid Email")

# re.sub - replaces the text
text = "My number is 9876"
print(re.sub(r"\d+", "XXXX", text))

# re.split
text = "apple,orange;banana"
print(re.split(r"[;,]", text))

# re.compile
my_str= "abc1234AcbabcABC"
pattern = re.compile("abc")
matches = pattern.findall(my_str)

for match in matches:
    print(match)

"""
Types of Regex Assertions
Type	Syntax	Meaning
Positive Lookahead	(?=...)	Must be followed by
Negative Lookahead	(?!...)	Must NOT be followed by
Positive Lookbehind	(?<=...)	Must be preceded by
Negative Lookbehind	(?<!...)	Must NOT be preceded by
"""

import re

text = "50kg 30kg 20g"
print(re.findall(r"\d+(?=kg)", text))

print(re.findall(r"\d+(?!kg)", text))

text = "$100 $200 300"
print(re.findall(r"(?<=\$)\d+", text))

print(re.findall(r"(?<!\$)\d+", text))
