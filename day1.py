# print("Hello world")

# name ="ram"
# faculty="Computer Science"
# dob="17/05/2061"

# # string concatenation
# name = input("Enter your name: ")
# faculty = input("Enter your faculty: ")
# dob = input("Enter your DOB: ")
# address = input("Enter your address: ")

# print("Hello, my name is: " + name)
# print("My faculty is: " + faculty)
# print("My DOB is: " + dob)
# print("My address is: " + address)

# #check data types
# print("Type of name:", type(name))
# print("Type of faculty:", type(faculty))
# print("Type of dob:", type(dob))
# print("Type of address:", type(address))

# #multiple assignment
# name, faculty, dob, roll_no = "Roshan", "BCA", "2061-05-17", 12345

# #dta types
# print(type(name))
# print(type(faculty))
# print(type(dob))
# print(type(roll_no))

# #value swapping
# a = 10
# b = 20
# print("before swapping: a =", a,"b =", b)
# a, b =b, a
# print("before swapping: a =", a,"b =", b)

# #unpack list
# my_list = ["ram", 20, 30.0]

# name, *other = my_list

# print(my_list)
# name, age, height = my_list

# print("Name:",name )
# print("Age:",age )
# print("Height:",height )


# #creating class
# student_name = ["Alice", "Bob", "Charlie", "Daniya"]
# student_id = [1, 2, 3, 4]
# print(student_name)
# print(student_id)

# print(student_name[0])  # Alice
# print(student_name[1])  # Bob
# print(student_name[2])  # Charlie
# # print(student_name[3])  # Daniya

# # #accesing element in list with indexing (0-n)
# # list1= [1, 2, 3, 4, 5]
# # print(list1[0])
# # print(list1[0:3])
# # print("Even position:", list1[::2])
# # print("Odd position:", list1[1::2])

# # #list comprehension
# # passing_marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# # passing_marks = [mark for mark in passing_marks if mark <= 80]
# # print("Pass student: ",passing_marks)

# # #common methods
# # print(len(passing_marks))
# # print(max(passing_marks))
# # print(min(passing_marks))
# # print(sum(passing_marks))
 
# #Tuples cannot be changed after creation
# # student_record = ["Alice", 20, 85.5, "Computer Science"]
# # print("Student Record Tuple",student_record)

# # Accessing tuple elements
# # print("Name", student_record[0])
# # print("Age", student_record[1])

# #set automatically remove duplicates
# course_A = {"Alice","Bob", "Charlie", "Diama"}
# course_B = {"Charlie","Diama", "Eve", "Franks"}

# print("Course A students", course_A)
# print("Course B students", course_B)

# #Set operationns (great for finding overlaps)
# print("\nStudents in both courses:", course_A & course_B)
# print("Students in either course:", course_A | course_B)
# print("Only in course A:", course_A - course_B)
# print("Only in one course:", course_A ^ course_B)

# #Remove implicates from list using txt
# scores_with_implicates = [15, 32, 65, 75, 60, 70]
# unique_scores = list(set(scores_with_implicates))

print("\n --- Dictionaries ---")
print("="*50)

student = {
    "name": "Alice",
    "age": 20,
    "scores": [55, 65, 75, 85],
    "department": "Computer Science",
    "is_active": True
}

print("Student Dictionary")
print(student)
