# Check if string contains only digits
import re

text = "12345"

if re.fullmatch(r"\d+", text):
    print("Only digits")

# 2️⃣ Match a 10-digit mobile number
number = "9876543210"

if re.fullmatch(r"\d{10}", number):
    print("Valid 10-digit number")

# 3️⃣ Find all lowercase letters
text = "Hello World"
print(re.findall(r"[a-z]", text))

# 4️⃣ Extract all uppercase letters
text = "Python Is FUN"
print(re.findall(r"[A-Z]", text))

# 5️⃣ Match string that starts with "Hello"
text = "Hello Python"
print(bool(re.match(r"^Hello", text)))

# 6️⃣ Match string that ends with "world"
text = "Hello world"
print(bool(re.search(r"world$", text)))

# 7️⃣ Find all words separated by spaces
text = "Python is very easy"
print(re.findall(r"\w+", text))

# 8️⃣ Match exactly 5 characters
text = "Hello"
print(bool(re.fullmatch(r".{5}", text)))

# 9️⃣ Find all occurrences of "python" (case-sensitive)
text = "python is easy. python is powerful"
print(re.findall(r"python", text))

# 🔟 Replace spaces with underscores
text = "Python is easy"
print(re.sub(r"\s", "_", text))

