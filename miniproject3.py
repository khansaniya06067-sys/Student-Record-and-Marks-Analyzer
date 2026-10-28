subjects = ('Python','Maths','DBMS')
print(f"Subject:{subjects}")

numbers = int(input("how many students?"))

all_students = {} #Empty Dictionary

for i in range(numbers):
    student_ids = input("\nStudent_Id : ")
    student_name = input("Name : ")
    python_marks = int(input("Python marks : "))
    Maths_marks = int(input("Maths marks : "))
    Dbms_marks = int(input("DBMS marks : "))


    total = python_marks+Maths_marks+Dbms_marks
    average_marks = total/3
    status = None
    if average_marks>=75:
        status = "Distinction"
    elif average_marks>=40:
        status = "Pass"
    else:
        status = "Fail"

    #now we are store the record in Dictionary
    all_students[student_ids] = {
        "name": student_name,
        "python": python_marks,
        "maths": Maths_marks,
        "dbms": Dbms_marks,
        "total": total,
        "average": average_marks,
        "status": status
    }



print("\n----- STUDENT REPORT -----")
for x in all_students:
    y = all_students[x]
    print(f"ID: {x} | Name: {y['name']}")
    print(f"Python: {y['python']}, Maths: {y['maths']}, DBMS: {y['dbms']}")
    print(f"Total: {y['total']} | Average: {y['average']:.2f} | Result: {y['status']}")
    

print(f"\nUnique subjects: {'Python','Maths','DBMS'}")
print(f"Students recorded: {numbers}")
                               