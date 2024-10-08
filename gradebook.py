import os

# Innitialize the gradebook as an empty list to store student data
gradebook = []

# A function to display the menu
def display_menu():
    print("\n--------- Gradebook Menu -----------")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. View Subject Statistics")
    print("4. View Student Grades by admin No")
    print("5. Edit Student Grades")
    print("6. Print Gradebook")
    print("7. Display Menu")
    print("8. Clear Screen")
    print("9. Quit\n")

# A function to add a student with marks
def add_student():
    admin_no = input("Enter Admin No : ")
    name = input("Enter Student Name: ")
    science = float(input("Enter Science Marks (0-100): "))
    sst = float(input("Enter SST Marks (0-100): "))
    english = float(input("Enter English Marks (0-100): "))
    maths = float(input("Enter Maths Marks (0-100): "))

    # Adding the students data to the list 
    gradebook.append({
        'admin_no':admin_no,
        'name': name,
        'science': science,
        'sst': sst,
        'english': english,
        'maths': maths
    })
    print(f"{name} added successifully\n")

# A function to delete a student
def delete_student():
    admin_no = input("Enter Admin No of student to delete: ")
    for student in gradebook:
        if student['admin_no'] == admin_no:
            gradebook.remove(student)
            print(f"Student {student['name']} deleted successifully!")
    print(f"Student with Admin No {admin_no} not found.\n")

# Function to view basic statistics for each subject
def view_statistics():
    if not gradebook:
        print("No student in gradebook.")
        return
    
    subjects = ['science', 'sst', 'english', 'maths']
    for subject in subjects:
        marks = [student[subject] for student in gradebook]
        if marks:
            print(f"\nStatistics for {subject.capitalize()}:")
            print(f" Average: {sum(marks)/len(marks):.2f}")
            print(f" Max: {max:(marks)}")
            print(f" Min: {min(marks)}")
        else:
            print(f"No marks available for {subject}.\n")    

# Function to view grades for a specific student
def view_student_grades():
    admin_no = input("Enter Admin No to view grades: ")
    for student in gradebook:
        if student['admin_no'] == admin_no:
            print(f"\nGrades for {student['name']} (Admin No: {admin_no})")
            print(f"Science: {student['science']}")
            print(f"SST: {student['sst']}")
            print(f"English: {student['english']}")
            print(f"Maths: {student['maths']}\n")
            return
    print(f"Student with Admin No {admin_no} not found.\n")    

# Function to edit a student's grades
def edit_student_grades():
    admin_no = input("Enter Admin No edit grades")
    for student in gradebook:
        if student['admin_no'] == admin_no:
            print(f"\nEditing grades for {student['name']} (Admin No: {admin_no})")
            student['science'] = float(input("Enter new Science marks: "))
            student['sst'] = float(input("Enter new SST marks: "))
            student['english'] = float(input("Enter new English marks: "))
            student['maths'] = float(input("Enter new Maths marks: "))
            print("Grades updated successifully!\n")

# Function to print the entire grade book
def print_gradebook():
    if not gradebook:
        print("Gradebook is empty.")
        return
    print(f"\n{'Admin No':<10}{'Name':<15}{'Science':<8}{'SST':<8}{'English':<8}{'Math':<8}")
    for student in gradebook:
        print(f"{student['admin_no']:<10}{student['name']:<15}{student['science']:<8}{student['sst']:<8}{student['english']:<8}{student['maths']:<8}")
    print()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

# Main loop for the gradebook system
def main():
    display_menu()
    while True:
        choice = input("\nEnter your choice (1-9): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            view_statistics()
        elif choice == '4':
            view_student_grades()
        elif choice == '5':
            edit_student_grades()
        elif choice == '6':
            print_gradebook()
        elif choice == '7':
            display_menu()
        elif choice == '8':
            clear_screen()
        elif choice == '9':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the gradebook system
if __name__=="__main__":
    main()
         