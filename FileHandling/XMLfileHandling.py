import xml.etree.ElementTree as ET

tree = ET.parse(r"C:/Users\WINDOW 11\PycharmProjects\PythonAdvancedProgramming\Dataframes\student.xml")
root = tree.getroot()
print(root.tag)

for student in root:
    print(student.tag)

for student in root:
    name = student.find("name").text
    branch = student.find("branch").text
    print(name, branch)

for student in root:
    print(student.get("id"))

print(root.find("student"))
print(root.findall("student"))

name = student.findtext("name")
print(name)

#Access Specific Element (Using Condition)
for student in root:
    if student.get("id") == "101":
        print(student.find("name").text)

#Modify XML Data
for student in root:
    if student.get("id") == "102":
        student.find("branch").text = "IT"

#Adding the new Elements:
new_student = ET.SubElement(root, "student", id="103")
ET.SubElement(new_student, "name").text = "Suresh"
ET.SubElement(new_student, "branch").text = "ME"

tree.write(r"C:\Users\WINDOW 11\PycharmProjects\PythonAdvancedProgramming\Dataframes\student.xml", encoding="utf-8", xml_declaration=True)
