import csv

#Reading the file of CSV
with open("C://Users//WINDOW 11//PycharmProjects//PythonAdvancedProgramming//Dataframes//CSVexample.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Writing to the CSV file
with open("C://Users//WINDOW 11//PycharmProjects//PythonAdvancedProgramming//Dataframes//WritingCSV.csv", "w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "age"])
    writer.writerow([1, "Ramesh", 22])
    writer.writerow([2, "Anil", 23])

#Updating the CSV files
