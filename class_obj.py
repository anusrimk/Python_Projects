# class students:
#     def _init_(self,name):
#         self.name=name
#         self.marks=[]
#     def enterMarks(self):
#         for i in range (3):
#             m=int(input("Enter the marks of %s in student %d:  "%(self.name,i+1)))
#             self.marks.append(m)
#     def display(self):
#         print(self.name," got ",self.marks)
    
# s1=students("Anusri")
# s1.enterMarks()
# s2=students("Karmokar")
# s2.enterMarks()
# s1.display()
# s2.display()




# class students:
#     def __init__(self, name):
#         count=0
#         self.name = name
#         self.marks = []

#     def enterMarks(self):
#         for i in range(3):
#             m = int(input("Enter the marks of %s in student %d: " % (self.name, i + 1)))
#             self.marks.append(m)
#             # students.count+=1
#             # print(students.count())

#     def display(self):
#         print(self.name, " got ", self.marks)

# s1 = students("Anusri")
# s1.enterMarks() 
# s2 = students("Karmokar")
# s2.enterMarks()
# s1.display()
# s2.display()




# class Student:
#     count = 0 

#     def __init__(self):
#         self.name = input("Enter the name: ")
#         self.age = int(input("Enter the age: "))
#         self.department = input("Enter the department (PGDM/B.Tech): ").capitalize() 
#         Student.count += 1

#     def display(self):
#         print("Name: ", self.name, "Age: ", self.age, "Department:", self.department)

# # Welcome message
# print(""" 
# STUDENT ADMIT
# ------------------""")
# pgdm_students = []
# btech_students = []

# while True:
#     new_student = Student()

#     new_student.display()

#     if new_student.department == 'P':
#         pgdm_students.append(new_student)
#     elif new_student.department == 'B':
#         btech_students.append(new_student)

#     user_input = input("Do you want to enter another student? (yes/no): ").lower()

#     if user_input != 'yes':
#         break 


# print("\nPGDM Department Students:")
# for student in pgdm_students:
#     student.display()

# print("\nB.Tech Department Students:")
# for student in btech_students:
#     student.display()


# print("\nTotal number of students:", Student.count)





# class ITM:
#     count = 0
#     btechcount=0
#     pgdmcount=0
#     def get(self):
#         self.name = input("Enter the name of the student: ")
#         self.age = int(input("Enter the age: "))
#         self.dep=int(input("Enter the department 1.B.Tech/2.PGDM "))
#         ITM.count += 1
#         if self.dep==1:
#             ITM.btechcount+=1
#         else:
#             ITM.pgdmcount+=1

#     def display(self):
#         if (self.dep==1):
#             print("Name:", self.name)
#             print("Age:", self.age)
#             print("Department: BTECH")
#             print()
#         elif (self.dep==2):
#             print("Name:", self.name)
#             print("Age:", self.age)
#             print("Deparment: PGDM")
#             print()

# students = int(input("Enter the number of students: "))

# list_btech = []
# list_pgdm=[]
# for i in range(students):
#     student = ITM()
#     student.get()
#     if (student.dep==1):
#         list_btech.append(student)
#     else:
#         list_pgdm.append(student)
#     print("\nStudent Details:")
#     if (student.dep==1):
#         for student in list_btech:
#             student.display()
#     print("__________________")
#     if(student.dep==2):
#         for student in list_pgdm:
#             student.display()

# print("\nTotal Admissions yet:", ITM.count)



class ITM:
    count = 0
    def get(self):
        self.name = input("Enter the name of the student: ")
        self.age = int(input("Enter the age: "))
        self.dep = int(input("Enter the department (1 for B.Tech, 2 for PGDM): "))
        ITM.count += 1

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        if self.dep == 1:
            print("Department: B.Tech")
        elif self.dep == 2:
            print("Department: PGDM")
        print()


students = int(input("Enter the number of students: "))

btech_students = []
pgdm_students = []

for i in range(students):
    student = ITM()
    student.get()
    
    if student.dep == 1:
        btech_students.append(student)
    elif student.dep == 2:
        pgdm_students.append(student)

print("\nB.Tech Students:")
for student in btech_students:
    student.display()

print("\nPGDM Students:")
for student in pgdm_students:
    student.display()

print("\nTotal Admissions yet:", ITM.count)