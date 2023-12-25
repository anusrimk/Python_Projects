#to print the name of the topper and his/her marks in 4 subjects wherein the 
# marks are specified as a list in the tuple topper
# Define a nested tuple with names and marks for four subjects

# Calculate the total marks for each student and find the topper

# If you want to print the specific marks of the topper as well:
# Find the index of the topper in the topper tuple

# Print the name of the topper and their marks
# Use topper_name to access the correct student's marks
# Also, use topper_marks instead of attempting to access topper[topper_name]


topper = (
    ("Anusri", [100, 95, 92, 98]),
    ("Piyush", [88, 92, 78, 90]),
    ("Garvit", [95, 89, 84, 91]),)

topper_name = ""
topper_marks = 0

for student, marks in topper:
    total_marks = sum(marks)
    
    if total_marks > topper_marks:
        topper_name = student
        topper_marks = total_marks



topper_index = [student[0] for student in topper].index(topper_name)

print(("The topper is", topper_name, "with marks:", topper_marks,("Marks are: ", topper[topper_index][1])))