 
 
def add_student():
    global stud_name, stud_rollnu, stud_age, stud_cgpa,student_rec
    print("to add new student record")
    stud_name=input("enter student name :")
    stud_rollnu=int(input("enter student rollnumber :"))
    stud_age=int(input("enter student age:"))
    stud_cgpa=float(input("enter student cgpa :"))
    student_rec={"student name:":stud_name,"student roll number:":stud_rollnu,"student age:":stud_age,"student cgpa:":stud_cgpa}
    print("student details added succesfully")
def display_student():
    global stud_name, stud_rollnu, stud_age, stud_cgpa,student_rec
    print("student record")
    print("student name:",stud_name)
    print("student roll number:",stud_rollnu)
    print("student age:",stud_age)
    print("student cgpa:",stud_cgpa)
def search_student():
    global stud_name, stud_rollnu, stud_age, stud_cgpa,student_rec
    print("To Search for a student")
    search_roll=int(input("enter desired student rollnumber"))
    if(search_roll==stud_rollnu):
        print("match found")
        display_student()
    else:
        print("student details not found")
def update_student():
    print("To update the student details")
    global stud_name, stud_rollnu, stud_age, stud_cgpa,student_rec
    search_roll=int(input("enter desired student rollnumber"))
    if(search_roll==stud_rollnu):
        print("match found")
        stud_name=input("enter new name :")
        stud_rollnu=int(input("enter  new student rollnumber :"))
        stud_age=int(input("enter new student age :"))
        stud_cgpa=float(input("enter new student cgpa :"))
        print("student details updated succesfully")
        print("student name:",stud_name)
        print("student roll number:",stud_rollnu)
        print("student age:",stud_age)
        print("student cgpa:",stud_cgpa)
    else:
        print("student details not found")
def delete_student():
    print("To delete the student details")
    print("NOTE: Please enter updated student roll number")
    global stud_name, stud_rollnu, stud_age, stud_cgpa,student_rec
    search_roll=int(input("enter desired student rollnumber"))
    if(search_roll==stud_rollnu):
        print("match found")
        del student_rec
        print("Student details succesfully deleted")
    else:
        print("student details not found")
add_student()
display_student()
search_student()
update_student()
delete_student()
    
                   
    
    
    
