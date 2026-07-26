# Student Gradebook Manager - Lisa Hlongwane - Python Essentials 1

# Returns the average of a list of marks, or None if the list is empty
def calculate_average(marks):
  if len(marks) == 0:
      return None

  return sum(marks)/len(marks)


# Returns the highest and lowest mark as a tuple: (highest, lowest)
def highest_and_lowest(marks):
    highest = max(marks)
    lowest = min(marks)

    return highest, lowest
  

# Asks for a mark, validates it with try-except, returns the float or None
def read_valid_mark():
    try:
        mark = float(input("Mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
            return None

        return mark

    except ValueError:
        print("That is not a number.")
        return None

# Adds a new student to the gradebook dictionary
def add_student(gradebook):
    name = input("Student name: ").strip()

    if name == "":
        print("Student name cannot be blank.")
        return

    if name in gradebook:
        print(f"{name} already exists.")
    else:
        gradebook[name] = []
        print(f"{name} added.")

# Adds one validated mark to an existing student
def add_mark(gradebook):
    name = input("Student name: ")

    if name not in gradebook:
        print("Student not found.")
        return

    mark = read_valid_mark()

    if mark is None:
        return

    gradebook[name].append(mark)
    print("Mark added.")

# Prints every student with marks and average
def view_all(gradebook):
    if len(gradebook) == 0:
        print("No students yet.")
        return

    for student, marks in gradebook.items():
        if len(marks) == 0:
            print(f"{student}: No marks")
        else:
            average = calculate_average(marks)
            print(f"{student}: {marks} - Average: {average:.2f}")

# Prints one student's full summary
def student_summary(gradebook):
    name = input("Student name: ")

    if name not in gradebook:
        print("Student not found.")
        return

    marks = gradebook[name]

    if len(marks) == 0:
        print(f"{name} has no marks yet.")
        return

    average = calculate_average(marks)
    highest, lowest = highest_and_lowest(marks)

    print(f"\nStudent: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")

# Prints class statistics including pass/fail lists
def class_statistics(gradebook):
    if len(gradebook) == 0:
        print("No students yet.")
        return

    all_marks = []
    passing = []
    failing = []
    top_student = None
    highest_average = -1

    for student, marks in gradebook.items():

        if len(marks) == 0:
            print(f"{student}: no marks yet")
            continue

        average = calculate_average(marks)

        all_marks.extend(marks)

        if average >= 50:
            passing.append(student)
        else:
            failing.append(student)

        if average > highest_average:
            highest_average = average
            top_student = student

    if len(all_marks) == 0:
        print("No marks available.")
        return

    class_average = sum(all_marks) / len(all_marks)

    print(f"\nTotal students: {len(gradebook)}")
    print(f"Class average: {class_average:.2f}")
    print(f"Top student: {top_student}")
    print(f"Passing: {passing}")
    print(f"Failing: {failing}")

# Removes a student after y/n confirmation
def remove_student(gradebook):
    name = input("Student name: ")

    if name not in gradebook:
        print("Student not found.")
        return

    confirm = input(f"Delete {name}? (y/n): ")

    if confirm.lower() == "y":
        del gradebook[name]
        print("Student removed.")
    else:
        print("Cancelled.")

# ---- main program ----

gradebook = {}
while True:
# print the menu, read the choice, call the right function
    print("\n STUDENT GRADEBOOK MANAGER ")
    print("1. Add a student")
    print("2. Add a mark")
    print("3. View all students")
    print("4. Student summary")
    print("5. Class statistics")
    print("6. Remove a student")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        add_student(gradebook)

    elif choice == "2":
        add_mark(gradebook)

    elif choice == "3":

        view_all(gradebook)

    elif choice == "4":
        student_summary(gradebook)

    elif choice == "5":
        class_statistics(gradebook)

    elif choice == "6":
        remove_student(gradebook)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 7.")
